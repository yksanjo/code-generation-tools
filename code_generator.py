"""
Code Generation Template Tool

This script provides tools for generating code from templates.
Features include:
- Project scaffolding from templates
- File generation from templates
- Customizable template system
"""

import os
import json
import argparse
from pathlib import Path
from string import Template
from typing import Dict, Any, List
import re


class TemplateEngine:
    """
    A simple template engine for code generation.
    """
    
    def __init__(self, templates_dir: str = None):
        self.templates_dir = Path(templates_dir) if templates_dir else Path(__file__).parent / "templates"
        self.templates_dir.mkdir(exist_ok=True)
        
        # Create default templates if they don't exist
        self._create_default_templates()
    
    def _create_default_templates(self):
        """
        Create default templates for common use cases.
        """
        # Python package template
        python_pkg_template = '''"""
$package_name package

Created on $date
"""

__version__ = "0.1.0"
__author__ = "$author"

def main():
    """
    Main function for $package_name
    """
    print("$package_name version {__version__}")


if __name__ == "__main__":
    main()
'''
        
        # Python class template
        python_class_template = '''"""
$module_name module

Created on $date
"""

class $class_name:
    """
    A class representing $class_name
    """
    
    def __init__(self$constructor_params):
        """
        Initialize the $class_name instance.
        """
$constructor_body

    def __str__(self):
        """
        String representation of the $class_name instance.
        """
        return f"$class_name()"

    def __repr__(self):
        """
        Developer-friendly representation of the $class_name instance.
        """
        return f"$class_name()"
'''
        
        # Python test template
        python_test_template = '''"""
Tests for $module_name
"""

import pytest
from $module_name import $class_name


class Test$class_name:
    """
    Test cases for $class_name class
    """
    
    def test_initialization(self):
        """
        Test initialization of $class_name
        """
        obj = $class_name()
        assert obj is not None

    def test_string_representation(self):
        """
        Test string representation of $class_name
        """
        obj = $class_name()
        assert isinstance(str(obj), str)
'''
        
        # Create templates directory if needed
        (self.templates_dir / "python").mkdir(exist_ok=True)
        
        # Write default templates
        templates = {
            "python/package.py": python_pkg_template,
            "python/class.py": python_class_template,
            "python/test.py": python_test_template
        }
        
        for template_path, content in templates.items():
            full_path = self.templates_dir / template_path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            if not full_path.exists():
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(content)
    
    def load_template(self, template_name: str) -> str:
        """
        Load a template by name.
        
        Args:
            template_name: Name of the template (with optional subdirectory)
            
        Returns:
            Template content as a string
        """
        template_path = self.templates_dir / template_name
        
        # If template doesn't have an extension, try adding .py
        if not template_path.suffix:
            template_path = template_path.with_suffix('.py')
        
        if not template_path.exists():
            raise FileNotFoundError(f"Template {template_path} does not exist")
        
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def generate_from_template(self, template_name: str, variables: Dict[str, Any]) -> str:
        """
        Generate code from a template with provided variables.
        
        Args:
            template_name: Name of the template to use
            variables: Dictionary of variables to substitute in the template
            
        Returns:
            Generated code as a string
        """
        template_content = self.load_template(template_name)
        template = Template(template_content)
        
        # Add default variables if not provided
        if 'date' not in variables:
            from datetime import datetime
            variables['date'] = datetime.now().strftime("%Y-%m-%d")
        
        return template.substitute(variables)
    
    def create_from_template(self, template_name: str, output_path: str, variables: Dict[str, Any]) -> None:
        """
        Create a file from a template with provided variables.
        
        Args:
            template_name: Name of the template to use
            output_path: Path where the generated file should be saved
            variables: Dictionary of variables to substitute in the template
        """
        generated_code = self.generate_from_template(template_name, variables)
        
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(generated_code)


class CodeGenerator:
    """
    Main class for code generation from templates.
    """
    
    def __init__(self, templates_dir: str = None):
        self.template_engine = TemplateEngine(templates_dir)
    
    def create_python_package(self, package_name: str, author: str = "Developer", 
                             output_dir: str = ".") -> None:
        """
        Create a basic Python package structure.
        
        Args:
            package_name: Name of the package
            author: Author name
            output_dir: Directory where the package should be created
        """
        output_path = Path(output_dir) / package_name
        output_path.mkdir(exist_ok=True)
        
        # Create __init__.py
        init_path = output_path / "__init__.py"
        variables = {
            "package_name": package_name,
            "author": author
        }
        self.template_engine.create_from_template(
            "python/package.py", 
            init_path, 
            variables
        )
        
        # Create main module
        main_path = output_path / "main.py"
        variables = {
            "package_name": package_name,
            "author": author
        }
        self.template_engine.create_from_template(
            "python/package.py", 
            main_path, 
            variables
        )
        
        print(f"Python package '{package_name}' created at {output_path}")
    
    def create_python_class(self, class_name: str, module_name: str = None, 
                           output_dir: str = ".", **kwargs) -> None:
        """
        Create a Python class file from template.
        
        Args:
            class_name: Name of the class to create
            module_name: Name of the module (defaults to class name in snake_case)
            output_dir: Directory where the file should be created
            **kwargs: Additional variables for the template
        """
        # Convert class name to snake_case for module name if not provided
        if module_name is None:
            module_name = re.sub(r'(?<!^)(?=[A-Z])', '_', class_name).lower()
        
        output_path = Path(output_dir) / f"{module_name}.py"
        
        # Prepare constructor parameters and body
        constructor_params = kwargs.get('constructor_params', '')
        constructor_body = kwargs.get('constructor_body', '        pass')
        
        variables = {
            "class_name": class_name,
            "module_name": module_name,
            "constructor_params": constructor_params,
            "constructor_body": constructor_body
        }
        
        self.template_engine.create_from_template(
            "python/class.py",
            output_path,
            variables
        )
        
        print(f"Python class '{class_name}' created at {output_path}")
    
    def create_test_file(self, class_name: str, module_name: str = None, 
                        output_dir: str = ".") -> None:
        """
        Create a test file for a Python class.
        
        Args:
            class_name: Name of the class to test
            module_name: Name of the module containing the class
            output_dir: Directory where the test file should be created
        """
        # Convert class name to snake_case for module name if not provided
        if module_name is None:
            module_name = re.sub(r'(?<!^)(?=[A-Z])', '_', class_name).lower()
        
        # Create test file name
        test_filename = f"test_{module_name}.py"
        output_path = Path(output_dir) / test_filename
        
        variables = {
            "class_name": class_name,
            "module_name": module_name
        }
        
        self.template_engine.create_from_template(
            "python/test.py",
            output_path,
            variables
        )
        
        print(f"Test file for '{class_name}' created at {output_path}")
    
    def list_templates(self) -> List[str]:
        """
        List all available templates.
        
        Returns:
            List of template names
        """
        templates = []
        for root, dirs, files in os.walk(self.template_engine.templates_dir):
            for file in files:
                if file.endswith('.py'):
                    rel_path = Path(root).relative_to(self.template_engine.templates_dir)
                    template_name = str(rel_path / file)
                    if template_name.startswith('.'):
                        template_name = template_name[2:]  # Remove './'
                    templates.append(template_name)
        return templates


def main():
    """
    Main function to demonstrate the CodeGenerator capabilities.
    """
    parser = argparse.ArgumentParser(description='Code Generation Template Tool')
    parser.add_argument('command', choices=['list', 'create-package', 'create-class', 'create-test'], 
                       help='Command to execute')
    parser.add_argument('--name', required=True, help='Name for the generated code element')
    parser.add_argument('--module', help='Module name (optional, defaults to name)')
    parser.add_argument('--author', default='Developer', help='Author name')
    parser.add_argument('--output', default='.', help='Output directory (default: current directory)')
    parser.add_argument('--constructor-params', help='Constructor parameters for class')
    parser.add_argument('--constructor-body', help='Constructor body for class')
    
    args = parser.parse_args()
    
    generator = CodeGenerator()
    
    if args.command == 'list':
        templates = generator.list_templates()
        print("Available templates:")
        for template in templates:
            print(f"  - {template}")
    
    elif args.command == 'create-package':
        generator.create_python_package(
            package_name=args.name,
            author=args.author,
            output_dir=args.output
        )
    
    elif args.command == 'create-class':
        generator.create_python_class(
            class_name=args.name,
            module_name=args.module,
            output_dir=args.output,
            constructor_params=args.constructor_params or '',
            constructor_body=args.constructor_body or '        pass'
        )
    
    elif args.command == 'create-test':
        generator.create_test_file(
            class_name=args.name,
            module_name=args.module,
            output_dir=args.output
        )


if __name__ == "__main__":
    main()