# LeetCode Scratch

用于记录刷题过程中的代码实现与练习笔记，目前主要包含 Python 与 C++ 两套实现。

## 目录结构

```text
leetcode-scratch/
├─ py/            # Python 题解（文件名如 l121.py）
├─ c++/           # C++ 题解与基础结构（文件名如 l151.h / lcr122.h）
├─ LICENSE.txt
└─ README.md
```

## 命名规则

- `l<number>`: 对应 LeetCode 题号，例如 `l55.py`、`l151.h`
- `lcr<number>`: 对应 LeetCode LCR 系列题目，例如 `lcr122.h`

## 运行方式

### Python

在仓库根目录执行：

```powershell
python .\py\l121.py
```

### C++

当前 `c++/main.cpp` 作为本地调试入口，可按需替换 `#include` 的题解头文件后编译运行：

```powershell
g++ .\c++\main.cpp -std=c++17 -O2 -o main.exe
.\main.exe
```

## 说明

- 本仓库以个人练习为主，不保证所有题解均包含完整测试用例。
- 可在每次新增题解后，按同样命名规则新增对应文件，保持目录可检索性。
