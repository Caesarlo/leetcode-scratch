# LeetCode Scratch

用于记录 LeetCode / LCR 练习题的代码实现。当前仓库分成两条线：

- `py/`：Python 题解，按 `uv` 启动和管理
- `c++/`：C++ 题解，按 `.vscode` 里的 build / debug 配置编译运行

## 目录结构

```text
leetcode-scratch/
├─ py/                     # Python 题解
│  ├─ l121.py
│  ├─ l122.py
│  └─ ...
├─ c++/                    # C++ 题解与本地调试入口
│  ├─ main.cpp
│  ├─ l151.h
│  ├─ lcr122.h
│  └─ build/               # VS Code 构建产物输出目录
├─ .vscode/                # VS Code 编译、调试和 IntelliSense 配置
└─ README.md
```

## 命名规则

- `l<number>` 表示 LeetCode 题号，例如 `l121.py`、`l151.h`
- `lcr<number>` 表示 LCR 系列题目，例如 `lcr122.h`
- Python 题解统一放在 `py/`
- C++ 题解统一放在 `c++/`，通常以头文件形式组织，方便 `main.cpp` 引入调试

## Python

Python 部分以 `uv` 管理和运行。当前仓库没有提交 `pyproject.toml` / `uv.lock`，所以这里按“脚本直接执行”的方式说明。

### 运行单个题解

在仓库根目录执行：

```powershell
uv run python .\py\l121.py
```

如果你后续为 Python 部分补上依赖管理文件，可以直接改成：

```powershell
uv sync
uv run python .\py\l121.py
```

### 新增题解

1. 在 `py/` 下新增对应文件，例如 `l123.py`
2. 按题目写 `Solution` 类和测试代码
3. 用 `uv run python .\py\<file>.py` 本地验证

## C++

C++ 部分按 `.vscode/tasks.json` 和 `.vscode/launch.json` 的配置来跑。

### 编译

当前 VS Code 的默认 build task 是编译“当前活动文件”：

- 先创建 `c++/build/`
- 再用 `g++.exe -std=c++17 -g`
- 输出到 `c++/build/<当前文件名>.exe`

也就是说，你在 VS Code 里打开 `c++/main.cpp` 或某个题解头文件后，直接执行 build 即可。

### 调试

调试配置是 `Debug C++ (gdb, active file)`，它会：

- 先触发 `build active file (g++)`
- 再用 `gdb.exe` 启动生成的可执行文件
- 可执行文件路径固定为 `c++/build/<当前文件名>.exe`

### 本地入口

`c++/main.cpp` 是当前本地测试入口。通常做法是：

1. 在 `main.cpp` 中 `#include` 你要调试的题解头文件
2. 构造输入并调用 `Solution`
3. 用 VS Code 的 build/debug 任务直接运行

### 手动命令

如果你不通过 VS Code，也可以手动编译：

```powershell
g++ .\c++\main.cpp -std=c++17 -g -o .\c++\build\main.exe
.\c++\build\main.exe
```

## IntelliSense

`.vscode/c_cpp_properties.json` 当前使用：

- `compilerPath` 指向 WinLibs 的 `g++.exe`
- `cppStandard` 为 `c++17`
- `intelliSenseMode` 为 `windows-gcc-x64`
- `includePath` 覆盖整个工作区

这意味着 C++ 代码和头文件可以按仓库内相对路径直接引用。

## 备注

- 这个仓库主要是个人刷题草稿和实现记录，不保证每个文件都包含完整的单元测试。
- `c++/build/` 是编译产物目录，不应该提交到仓库。
- 如果后续 Python 部分开始依赖第三方包，建议补上 `pyproject.toml` 和 `uv.lock`，让 `uv sync` 成为标准入口。
