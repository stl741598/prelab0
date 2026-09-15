import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path




SCRIPT_DIR = Path(__file__).resolve().parent
BUNDLE_DIR = os.environ.get("CLASSROOM50_BUNDLE_DIR")

# Locally, test the repository containing this script.
# In Classroom 50, the student's repository is the working directory.
STUDENT_ROOT = Path.cwd() if BUNDLE_DIR else SCRIPT_DIR
INPUT_DIR = Path(BUNDLE_DIR) / "input" if BUNDLE_DIR else SCRIPT_DIR / "input"


def main():
    failures = 0

    with tempfile.TemporaryDirectory(prefix="phase0-") as temporary:
        temporary = Path(temporary)
        build_dir = temporary / "build"
        result_dir = temporary / "results"
        result_dir.mkdir()

        try:
            subprocess.run(
                ["cmake", "-S", str(STUDENT_ROOT), "-B", str(build_dir)],
                check=True,
            )
            subprocess.run(
                ["cmake", "--build", str(build_dir)],
                check=True,
            )
        except FileNotFoundError as error:
            print(f"BUILD FAILED: required program not found: {error.filename}")
            return 1
        except subprocess.CalledProcessError:
            print("BUILD FAILED")
            return 1

        candidates = [
            build_dir / "arbitrary",
            build_dir / "arbitrary.exe",
            build_dir / "Release" / "arbitrary.exe",
            ]
        executable = next((path for path in candidates if path.is_file()), None)

        if executable is None:
            print("BUILD FAILED: arbitrary executable was not created!!!!")
            return 1

        input_files = sorted(INPUT_DIR.glob("*.txt"))
        if not input_files:
            print("ERROR: no input test files were found")
            return 1

        for input_file in input_files:
            output_file = result_dir / input_file.name

            try:
                values = input_file.read_text().split()
                if len(values) != 2:
                    raise ValueError("input must contain exactly two integers")

                a, b = map(int, values)

                subprocess.run(
                    [str(executable), str(input_file), str(output_file)],
                    check=True,
                    timeout=10,
                )

                lines = output_file.read_text().splitlines()
            except (OSError, ValueError, subprocess.SubprocessError) as error:
                print(f"{input_file.stem}: FAILED ({error})")
                failures += 1
                continue

            expected = [
                f"1> {a}, {b}",
                f"2> {a + b}, {a - b}",
                f"3> {a % b}, {a * b}",
                "4> That's it!",
            ]

            identity_is_valid = (
                    len(lines) == 5
                    and re.fullmatch(r"[^,]+,\s*[^,]+,\s*\d+", lines[0].strip())
            )

            if identity_is_valid and lines[1:] == expected:
                print(f"{input_file.stem}: PASSED")
            else:
                print(f"{input_file.stem}: FAILED")
                print("Expected four result lines:", expected)
                print("Actual output:", lines)
                failures += 1

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())