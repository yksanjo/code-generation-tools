# Code Generation Tools

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/status-stable-success.svg)](https://shields.io/)
[![Template System](https://img.shields.io/badge/template-system-9b59b6.svg)](https://shields.io/)

> Template-based code generation tools for accelerating development

## 🚀 Overview

Code Generation Tools is a comprehensive suite of template-based utilities for generating code, creating project scaffolds, and accelerating development workflows. These tools help developers quickly create standard code structures and reduce boilerplate, enabling faster development cycles.

## ✨ Features

- **Template System**: Flexible template-based code generation
- **Project Scaffolding**: Create standard project structures with a single command
- **Class Generation**: Generate Python class files with standard structure
- **Test Generation**: Create test files for your classes
- **Custom Templates**: Create and use your own templates
- **Command-Line Interface**: Easy-to-use CLI for automation scripts

## 📸 Screenshots

![Code Generation Demo](https://placehold.co/800x400/4a5568/ffffff?text=Code+Generation+Tools+Demo)

*Example of generating a Python class with custom parameters*

![Template System](https://placehold.co/800x400/2d3748/ffffff?text=Template+System+Features)

*Using custom templates for code generation*

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- pip

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/code-generation-tools.git
   cd code-generation-tools
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. The tools are now ready to use from the command line.

### Standalone Installation

You can also install the tools as a standalone package:

```bash
pip install code-generation-tools
```

## 🎮 Usage

### Command-Line Interface

The tool provides a command-line interface for all operations:

#### List Available Templates

View all available templates:

```bash
python code_gen_tool.py list
```

#### Create a Python Package

Create a new Python package with standard structure:

```bash
python code_gen_tool.py create-package my_new_package --author "Your Name"
```

This creates a directory with:
- `__init__.py` - Package initialization file
- `main.py` - Main application file with basic structure
- Standard files following Python packaging conventions

#### Create a Python Class

Generate a Python class file with standard structure:

```bash
python code_gen_tool.py create-class MyClass --constructor-params ", name: str, value: int" --constructor-body "        self.name = name\n        self.value = value"
```

#### Create a Test File

Generate a test file for an existing class:

```bash
python code_gen_tool.py create-test MyClass
```

### Python API

For integration with other tools:

```python
from code_generation.code_generator import CodeGenerator

generator = CodeGenerator()

# Create a Python package
generator.create_python_package("my_package", "Author Name")

# Create a Python class
generator.create_python_class("MyClass", constructor_params=", name: str", 
                             constructor_body="        self.name = name")

# Create a test file
generator.create_test_file("MyClass")

# List available templates
templates = generator.list_templates()
```

## 🧪 Examples

### Creating a Complete Project Structure

```bash
# Create a new package
$ python code_gen_tool.py create-package my_api --author "Jane Developer"

# Create a model class
$ python code_gen_tool.py create-class UserModel --constructor-params ", username: str, email: str" --constructor-body "        self.username = username\n        self.email = email"

# Create a test file for the model
$ python code_gen_tool.py create-test UserModel
```

### Using Custom Templates

```python
from code_generation.code_generator import TemplateEngine

# Create a custom template
engine = TemplateEngine()

# Define custom variables
variables = {
    "class_name": "APIHandler",
    "module_name": "api_handler",
    "constructor_params": "",
    "constructor_body": "        self.base_url = 'https://api.example.com'"
}

# Generate code from template
generated_code = engine.generate_from_template("python/class.py", variables)

# Save to file
engine.create_from_template("python/class.py", "api_handler.py", variables)
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add examples/tests for your changes
5. Update documentation
6. Submit a pull request

### Adding New Templates

To add a new template:

1. Create a new template file in the `templates/` directory
2. Use Python's `string.Template` syntax for variables
3. Update the documentation with your new template
4. Submit a pull request

### Development Setup

```bash
git clone https://github.com/yourusername/code-generation-tools.git
cd code-generation-tools
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

- Check the [documentation](docs/)
- Open an [issue](https://github.com/yourusername/code-generation-tools/issues)
- Submit a [pull request](https://github.com/yourusername/code-generation-tools/pulls)

## 🙏 Acknowledgments

- Inspired by code generation tools in the development community
- Built with Python's string.Template module
- Designed with developer productivity in mind

---

<div align="center">

**Made with ❤️ for faster development**

[Back to Top](#code-generation-tools)

</div>