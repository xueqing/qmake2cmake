# qmake2cmake
 
 本仓库包含将 QMake 项目转为 CMake 项目的 Python 脚本。

 ## 目标

 qmake2cmake 工具创建 `CMakeLists.txt`，覆盖了被转换的 `.pro` 文件的大多常见属性。生成的 CMake 项目可用作基础，且很可能需要手动调整。 

 QMake 结构中不能转换的在 CMake 项目中成为注释。

## 非目标

以下 QMake 结构不能被转换：

- `TEMPLATE = aux` 项目
- 自定义 `.prf` 文件
- 额外的编译器
- 额外的目标
- 安装规则

# 要求

- [Python 3.7](https://www.python.org/downloads/)
- `pipenv` 或 `pip` 用于管理模块

## Python 模块

由于 Python 有很多方法处理项目，因此你有几个选项来安装脚本的依赖项：

### 使用 `pipenv`

依赖项在 `Pipfile` 中指定，因此你只需要运行 `pipenv install`，它将自动创建一个虚拟环境，你可以使用 `pipenv shell` 激活该环境。

### 使用 `pip`

为了避免与已安装的其他软件包发生冲突，强烈建议使用虚拟环境。

- 创建环境：`python3 -m venv env --prompt qmake2cmake`，
- 激活环境：`source env/bin/activate`（在 Windows 上：`env\Scripts\activate.bat`）
- 安装要求：`pip install -r requirements.txt`

如果上面的 `pip install` 命令不起作用，请尝试：

```sh
python3.7 -m pip install -r requirements.txt
```

# 安装

你可以通过 `pip install qmake2cmake` 直接安装此软件包。

如果你正在开发新功能或想要安装最新的仓库版本，请通过运行 `pip install -e` 进行可编辑的构建。

# 用法

安装 `qmake2cmake` 包后，在 Python 环境的 bin/ 目录中将有两个脚本可用：`qmake2cmake` 和 `qmake2cmake_all`。

以下调用将单个 QMake 项目文件转换为 CMake：

```sh
qmake2cmake ~/projects/myapp/myapp.pro --min-qt-version 6.3
```

有必要指定构建项目的最低 Qt 版本。使用 `--min-qt-version` 选项或环境变量 `QMAKE2CMAKE_MIN_QT_VERSION`。

默认情况下，`CMakeLists.txt` 放在 `.pro` 文件旁边。

要在不同的位置生成 `CMakeLists.txt`，请使用 `-o` 选项：

```sh
qmake2cmake ~/projects/myapp/myapp.pro --min-qt-version 6.3 -o ~/projects/myapp-converted/CMakeLists.txt
```

要转换整个项目树，请将项目目录传递给 `qmake2cmake_all`：

```sh
qmake2cmake_all ~/projects/myapp --min-qt-version 6.3
```

# 贡献

主要源代码仓库托管在 [codereview.qt-project.org](https://codereview.qt-project.org/q/project:qt/qmake2cmake)。

请参阅 [Qt 贡献指南](https://wiki.qt.io/Qt_Contribution_Guidelines)页面，[设置 Gerrit](https://wiki.qt.io/Setting_up_Gerrit) 和 [Gerrit 介绍](https://wiki.qt.io/Gerrit_Introduction)，了解更多有关如何上传补丁以供审核的详细信息。

## 代码风格和测试

你可以通过执行以下命令运行 linter (`mypy`)、代码样式检查器 (`flake8`, `black`) 和测试 (`pytest`)：

```sh
make test
```

每个 `make mypy`、`make flake8`、`make black_format_check`、`make pytest` 也有单独的 make 目标。

你可以使用 [black](https://black.readthedocs.io/en/stable/) 自动格式化代码：

```sh
make format
```

# 发布新版本

根据语义版本控制 2.0 增加 `setup.cfg` 中的版本号。

要构建和上传 `qmake2cmake`，你将需要 Python 模块 `build` 和 `twine`。

构建 wheel：

```sh
$ python -m build
```

上传到 testpypi：

```sh
$ twine upload --repository testpypi dist/<wheel-name>
```

在新的 venv 中安装上传的 wheel：

```sh
$ python -m venv fresh && . ./fresh/bin/activate
(fresh)$ pip install -i https://testpypi.python.org/pypi qmake2cmake --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple
```

如果安装成功，尝试转换一些东西。如果一切正常，将 wheel 上传到生产 pypi。

`$ twine upload --repository pypi dist/<wheel-name>`

建议在另一个新鲜的 venv 中试用这个 wheel。