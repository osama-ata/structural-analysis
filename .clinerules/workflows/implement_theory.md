# Workflow: Implement a Structural Analysis Theory

This workflow sets up your editor to implement a new theory and its corresponding tests. It opens the relevant files and provides a clear task prompt.

## Step 1: Get Theory Details

First, we need to know which theory you want to work on.

<ask_followup_question>
<variable_name>category_name</variable_name>
<prompt>What is the Category of the theory you want to implement? (e.g., "Beam Theory", "Plate/Shell Theory")</prompt>
</ask_followup_question>

<ask_followup_question>
<variable_name>theory_name</variable_name>
<prompt>What is the specific Theory Name? (e.g., "Euler-Bernoulli", "Timoshenko")</prompt>
</ask_followup_question>

## Step 2: Determine File Paths

Next, Cline will convert the category name into the correct snake_case filenames for the source and test modules.

<execute_command>
<description>Convert category to snake_case for filename</description>
<command>

# Note: This command is for Cline's internal logic to derive the path

# It converts "Plate/Shell Theory" into "plate_shell_theory"

category_filename=$(echo "{{category_name}}" | tr '[:upper:]' '[:lower:]' | sed 's/ /_/g' | sed 's/\//_/g' | sed 's/-/_/g')
echo "Source file will be src/structural_analysis/${category_filename}.py"
echo "Test file will be tests/test_${category_filename}.py"
</command>
<requires_approval>false</requires_approval>
</execute_command>

## Step 3: Open Files and Set Up Task

Cline will now open the files and create a task to guide your implementation.

<new_task>
<description>Implement the '{{theory_name}}' theory and its tests.</description>
<instructions>
Please perform the following steps:

1. **Open Source File**: Cline will open `src/structural_analysis/{{category_filename}}.py`.
2. **Open Test File**: Cline will open `tests/test_{{category_filename}}.py`.
3. **Implement Logic**: In the source file, find the method for `{{theory_name}}` and implement its logic. Use the docstring and comments to guide GitHub Copilot.
4. **Write Tests**: In the test file, write one or more `pytest` functions to verify your implementation.
5. **Run Tests & Lint**: Once complete, run the following commands in the terminal:
    - `pytest tests/test_{{category_filename}}.py`
    - `ruff format . && ruff check . --fix`
</instructions>

</new_task>
