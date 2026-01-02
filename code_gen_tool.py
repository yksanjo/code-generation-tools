#!/usr/bin/env python3
"""
Command-line interface for the Code Generation Template Tool.
"""

import sys
import os
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from code_generation.code_generator import CodeGenerator


def main():
    """
    Main CLI function for the code generator.
    """
    if len(sys.argv) < 2:
        print("Usage: code_gen_tool.py <command> [options]")
        print("Commands:")
        print("  list                    - List all available templates")
        print("  create-package NAME     - Create a Python package with given NAME")
        print("  create-class NAME       - Create a Python class with given NAME")
        print("  create-test NAME        - Create a test file for class with given NAME")
        print("")
        print("Options:")
        print("  --module MODULE         - Specify module name (for create-class and create-test)")
        print("  --author AUTHOR         - Specify author name (for create-package)")
        print("  --output OUTPUT_DIR     - Specify output directory (default: current directory)")
        print("  --constructor-params    - Constructor parameters (for create-class)")
        print("  --constructor-body      - Constructor body (for create-class)")
        return

    command = sys.argv[1]
    generator = CodeGenerator()
    
    if command == "list":
        templates = generator.list_templates()
        print("Available templates:")
        for template in templates:
            print(f"  - {template}")
    
    elif command == "create-package":
        if len(sys.argv) < 3:
            print("Error: Package name is required")
            return
        
        name = sys.argv[2]
        author = "Developer"  # default
        output = "."  # default
        
        # Parse additional options
        i = 3
        while i < len(sys.argv):
            if sys.argv[i] == "--author" and i + 1 < len(sys.argv):
                author = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] == "--output" and i + 1 < len(sys.argv):
                output = sys.argv[i + 1]
                i += 2
            else:
                print(f"Unknown option: {sys.argv[i]}")
                return
        
        generator.create_python_package(name, author, output)
    
    elif command == "create-class":
        if len(sys.argv) < 3:
            print("Error: Class name is required")
            return
        
        name = sys.argv[2]
        module = None
        output = "."  # default
        constructor_params = ""
        constructor_body = "        pass"
        
        # Parse additional options
        i = 3
        while i < len(sys.argv):
            if sys.argv[i] == "--module" and i + 1 < len(sys.argv):
                module = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] == "--output" and i + 1 < len(sys.argv):
                output = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] == "--constructor-params" and i + 1 < len(sys.argv):
                constructor_params = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] == "--constructor-body" and i + 1 < len(sys.argv):
                constructor_body = sys.argv[i + 1]
                i += 2
            else:
                print(f"Unknown option: {sys.argv[i]}")
                return
        
        generator.create_python_class(
            name, 
            module, 
            output, 
            constructor_params=constructor_params,
            constructor_body=constructor_body
        )
    
    elif command == "create-test":
        if len(sys.argv) < 3:
            print("Error: Class name is required")
            return
        
        name = sys.argv[2]
        module = None
        output = "."  # default
        
        # Parse additional options
        i = 3
        while i < len(sys.argv):
            if sys.argv[i] == "--module" and i + 1 < len(sys.argv):
                module = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] == "--output" and i + 1 < len(sys.argv):
                output = sys.argv[i + 1]
                i += 2
            else:
                print(f"Unknown option: {sys.argv[i]}")
                return
        
        generator.create_test_file(name, module, output)
    
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()