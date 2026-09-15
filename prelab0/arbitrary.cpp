// 包含文件读写相关的标准库头文件
#include <fstream>
// 包含控制台输入输出标准库头文件（std::cerr 需要这个）
#include <iostream>

// main函数：程序入口
// argc：argument count，命令行参数的总个数
// argv：argument vector，字符串数组，存放所有命令行参数
// argv[0] 永远是程序本身的名字；argv[1]是第1个参数，argv[2]第2个参数
int main(int argc, char* argv[]) {
    // 判断：参数总数必须等于3（程序名 + 输入文件名 + 输出文件名）
    if (argc != 3) {
        // std::cerr：标准错误输出流，专门打印错误信息
        // 提示用户正确使用格式
        std::cerr << "Usage: " << argv[0]
                  << " <input_file> <output_file>\n";
        // return 1：程序异常退出，返回非0代表出错
        return 1;
    }

    // 创建文件读取流对象 input，尝试打开 argv[1] 指定的输入文件
    std::ifstream input(argv[1]);
    // 如果文件打开失败（找不到文件/权限不足）
    if (!input) {
        std::cerr << "Failed to open input file: " << argv[1] << '\n';
        return 1;
    }

    // 定义两个 long long 类型变量，可以存储范围很大的整数
    long long a;
    long long b;
    // 从打开的 input 文件里读取两个整数，存入 a 和 b
    // 如果读取失败（文件内容不是数字、数字不够），进入if分支报错
    if (!(input >> a >> b)) {
        std::cerr << "Input file must contain two integers.\n";
        return 1;
    }

    // 判断第二个数字不能为0，因为取模运算 a%b 中b=0会造成程序崩溃
    if (b == 0) {
        std::cerr << "The second integer must not be zero.\n";
        return 1;
    }

    // 创建文件写入流对象 output，打开/创建 argv[2] 指定的输出文件
    std::ofstream output(argv[2]);
    // 如果输出文件创建/打开失败
    if (!output) {
        std::cerr << "Failed to open output file: " << argv[2] << '\n';
        return 1;
    }

    // 向输出文件写入多行内容，<< 是输出写入符号
    output << "Mutian, Zhu, 1234567\n";          // 写入姓名学号
    output << "1> " << a << ", " << b << '\n';  // 写入原始读到的两个数字
    output << "2> " << a + b << ", " << a - b << '\n'; // 和、差
    output << "3> " << a % b << ", " << a * b << '\n'; // 取模、乘积
    output << "4> That's it!\n";

    // 程序正常结束，返回0表示运行成功
    return 0;
}

