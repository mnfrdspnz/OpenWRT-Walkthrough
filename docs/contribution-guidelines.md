# Contribution Guidelines

## 10.1 How to Contribute

**Forking the Repository:**

1. **Go to the Repository Page**:
   - Navigate to the GitHub repository you want to contribute to (e.g., `https://github.com/mnfrdspnz/OpenWRT-Walkthrough`).

2. **Fork the Repository**:
   - Click the "Fork" button in the top-right corner of the repository page. This will create a copy of the repository under your GitHub account.

3. **Clone the Forked Repository**:
   - Clone the forked repository to your local machine using the following command:
     ```bash
     git clone https://github.com/yourusername/OpenWRT-Walkthrough.git
     cd OpenWRT-Project
     ```

4. **Set Upstream Remote**:
   - Add the original repository as an upstream remote to keep your fork synchronized:
     ```bash
     git remote add upstream https://github.com/originalowner/OpenWRT-Walkthrough.git
     git fetch upstream
     ```

**Creating Pull Requests:**

1. **Create a New Branch**:
   - Create a new branch for your changes:
     ```bash
     git checkout -b feature-branch
     ```

2. **Make Changes**:
   - Make your changes to the repository in this new branch.

3. **Commit Changes**:
   - Commit your changes with a descriptive message:
     ```bash
     git add .
     git commit -m "Description of changes"
     ```

4. **Push Changes to Your Fork**:
   - Push your changes to the new branch on your fork:
     ```bash
     git push origin feature-branch
     ```

5. **Create a Pull Request**:
   - Go to the original repository on GitHub and click the "New pull request" button.
   - Select your fork and the branch with your changes, then click "Create pull request".
   - Provide a descriptive title and detailed description of your changes.

**Keeping Your Fork Updated:**

1. **Fetch and Merge Updates**:
   - Fetch and merge updates from the upstream repository:
     ```bash
     git fetch upstream
     git checkout main
     git merge upstream/main
     ```

2. **Push Updates to Your Fork**:
   - Push the updates to your fork:
     ```bash
     git push origin main
     ```

## 10.2 Code of Conduct

**Expected Behavior:**

1. **Respectful Communication**:
   - Use welcoming and inclusive language.
   - Respect differing viewpoints and experiences.
   - Gracefully accept constructive criticism.

2. **Collaboration and Cooperation**:
   - Be collaborative and support each other.
   - Show empathy towards other community members.

3. **No Discrimination or Harassment**:
   - Do not engage in or tolerate any form of harassment or discrimination based on race, gender, sexual orientation, disability, or any other protected characteristic.

**Guidelines for Contributors:**

1. **Adhere to Project Standards**:
   - Follow the coding standards and guidelines set by the project.
   - Write clear and concise commit messages.

2. **Submit Quality Contributions**:
   - Ensure your code is well-tested and bug-free.
   - Provide documentation and comments where necessary.

3. **Report Issues and Suggest Enhancements**:
   - Use the issue tracker to report bugs, suggest enhancements, and ask questions.

4. **Review and Improve Code**:
   - Participate in code reviews to help improve the code quality.

