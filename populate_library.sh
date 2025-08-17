#!/bin/bash

# Stop on Any error
set -e

# --- Configuration ---
SRC_DIR="src/structural_analysis"
CSV_FILE="structural_analysis_theories_comprehensive.csv"

# --- Pre-flight Check ---
if [ ! -f "$CSV_FILE" ]; then
    echo "❌ Error: The CSV file '$CSV_FILE' was not found."
    echo "Please place it in the root of your project directory."
    exit 1
fi

if [ ! -d "$SRC_DIR" ]; then
    echo "❌ Error: The source directory '$SRC_DIR' does not exist."
    echo "Please run the initialization script first."
    exit 1
fi

# --- Main Logic ---
echo "🚀 Starting library population from '$CSV_FILE'..."

# Clear existing modules to prevent duplicates, but keep __init__.py
find "$SRC_DIR" -type f -name "*.py" ! -name "__init__.py" -delete
rm -f "$SRC_DIR/__init__.py" # Recreate __init__.py from scratch
touch "$SRC_DIR/__init__.py"

# Use awk to process the CSV:
# The key change is adding gsub(/\//, "_", snake_cat) to handle slashes.
awk -F, '
NR > 1 {
    categories[$1] = 1
    theories[$1] = theories[$1] $2 ";"
    descriptions[$1,$2] = $3
    assumptions[$1,$2] = $4
    applications[$1,$2] = $5
    advantages[$1,$2] = $6
    limitations[$1,$2] = $7
}
END {
    for (cat in categories) {
        # Convert category name to a safe snake_case filename
        snake_cat = cat
        gsub(/ /, "_", snake_cat)
        gsub(/-/, "_", snake_cat)
        gsub(/\//, "_", snake_cat) # <--- THIS IS THE FIX
        snake_cat = tolower(snake_cat)
        filename = "'"$SRC_DIR"'" "/" snake_cat ".py"

        # Convert category name to CamelCase for the class name
        camel_cat = cat
        gsub(/ /, "", camel_cat)
        gsub(/-/, "", camel_cat)
        gsub(/\//, "", camel_cat)


        print "   - Creating module for: " cat

        # Write the class definition
        print "import numpy as np
from typing import Dict, Union, Optional, Literal, Any\n" > filename
        print "class " camel_cat ":" >> filename
        print "    \"\"\"" >> filename
        print "    Implements theories related to " cat "." >> filename
        print "    \"\"\"" >> filename

        # Split the theories and create methods
        split(theories[cat], theory_list, ";")
        for (i in theory_list) {
            theory_name = theory_list[i]
            if (theory_name == "") continue

            # Convert theory name to snake_case for the method name
            snake_theory = theory_name
            gsub(/([a-z0-9])([A-Z])/, "\\1_\\2", snake_theory)
            snake_theory = tolower(snake_theory)
            gsub(/ /, "_", snake_theory)
            gsub(/-/, "_", snake_theory)

            # Write the method stub and the detailed docstring
            print "" >> filename
            print "    def " snake_theory "(self, *args, **kwargs):" >> filename
            print "        \"\"\"" >> filename
            print "        " descriptions[cat, theory_name] "\n" >> filename
            print "        Key Assumptions:" >> filename
            print "        - " assumptions[cat, theory_name] "\n" >> filename
            print "        Primary Applications:" >> filename
            print "        - " applications[cat, theory_name] "\n" >> filename
            print "        Advantages:" >> filename
            print "        - " advantages[cat, theory_name] "\n" >> filename
            print "        Limitations:" >> filename
            print "        - " limitations[cat, theory_name] >> filename
            print "        \"\"\"" >> filename
            print "        # TODO: Implement the mathematical model for " theory_name >> filename
            print "        print(f\"Calculating result for {theory_name}...\")" >> filename
            print "        pass" >> filename
        }
    }
}' "$CSV_FILE"

# --- Generate the main __init__.py file ---
echo "   - Generating the main __init__.py API file..."
INIT_FILE="$SRC_DIR/__init__.py"

# Find all generated modules, get their snake_case and CamelCase names
for f in "$SRC_DIR"/*.py; do
    if [[ "$f" == *__init__.py ]]; then continue; fi
    
    filename=$(basename -- "$f")
    module_name="${filename%.*}"

    # Create CamelCase class name from snake_case module name
    class_name=$(echo "$module_name" | sed -r 's/(^|_)(\w)/\U\2/g')

    echo "from .$module_name import $class_name" >> "$INIT_FILE"
done

# Add the main StructuralAnalysis class
echo "" >> "$INIT_FILE"
echo "class StructuralAnalysis:" >> "$INIT_FILE"
echo '    """' >> "$INIT_FILE"
echo '    A comprehensive library for structural analysis theories.' >> "$INIT_FILE"
echo '    """' >> "$INIT_FILE"
echo "    def __init__(self):" >> "$INIT_FILE"

# Add initializers
for f in "$SRC_DIR"/*.py; do
    if [[ "$f" == *__init__.py ]]; then continue; fi
    filename=$(basename -- "$f")
    module_name="${filename%.*}"
    class_name=$(echo "$module_name" | sed -r 's/(^|_)(\w)/\U\2/g')
    echo "        self._${module_name} = ${class_name}()" >> "$INIT_FILE"
done

# Add properties
for f in "$SRC_DIR"/*.py; do
    if [[ "$f" == *__init__.py ]]; then continue; fi
    filename=$(basename -- "$f")
    module_name="${filename%.*}"
    # Format a user-friendly name for the docstring
    pretty_name=$(echo "$module_name" | sed 's/_/ /g' | sed -r 's/\b(\w)/\U\1/g')
    
    echo "" >> "$INIT_FILE"
    echo "    @property" >> "$INIT_FILE"
    echo "    def ${module_name}(self):" >> "$INIT_FILE"
    echo "        \"\"\"Provides access to ${pretty_name} methods.\"\"\"" >> "$INIT_FILE"
    echo "        return self._${module_name}" >> "$INIT_FILE"
done

echo "✅  Library population complete!"
echo "✨  Your source code in '$SRC_DIR' is now populated. Ready for implementation!"