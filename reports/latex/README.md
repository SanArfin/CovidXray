# Setting up Visual Studio Code with LaTeX Workshop

This guide provides a step-by-step walkthrough to set up Visual Studio Code (VS Code) with the LaTeX Workshop extension for a seamless LaTeX editing and compiling experience. Additionally, it covers the installation of prerequisites such as Perl and MiKTeX on both Windows and Linux systems.

---

## Prerequisites

1. **Install Visual Studio Code**
   - Download and install Visual Studio Code from the [official website](https://code.visualstudio.com/).

2. **Install Perl**
   - **Windows**:
     1. Download the Strawberry Perl installer from the [official website](https://strawberryperl.com/).
     2. Run the installer and follow the on-screen instructions to complete the installation.
   - **Linux**:
     1. Open a terminal and run:
        ```bash
        sudo apt update
        sudo apt install perl
        ```
        (For Debian-based distros; for other distros, use the appropriate package manager.)

3. **Install MiKTeX**
   - **Windows**:
     1. Download the MiKTeX installer from the [official website](https://miktex.org/download).
     2. Run the installer and follow the on-screen instructions.
   - **Linux**:
     1. Open a terminal and run:
        ```bash
        sudo apt update
        sudo apt install miktex
        ```
        (For Debian-based distros; for other distros, use the appropriate package manager.)
     2. After installation, run:
        ```bash
        miktexsetup finish
        initexmf --mkmaps
        ```

---

## Setting Up LaTeX Workshop in VS Code

1. **Install LaTeX Workshop Extension**
   - Launch Visual Studio Code.
   - Go to the Extensions view (`Ctrl+Shift+X` or click the Extensions icon in the sidebar).
   - Search for "LaTeX Workshop" and click `Install`.

2. **Configure LaTeX Workshop**
   - Open the VS Code settings (`Ctrl+,` or `File > Preferences > Settings`).
   - Search for `LaTeX Workshop` and ensure the following settings are configured:
     - Path to `pdflatex` if not already set (typically added automatically by MiKTeX).

3. **Test LaTeX Compilation**
   - Create a new `.tex` file and paste the following sample content:
     ```tex
     \documentclass{article}
     \begin{document}
     Hello, LaTeX!
     \end{document}
     ```
   - Save the file and click on `Build LaTeX project` in the LaTeX Workshop sidebar (or use the shortcut `Ctrl+Alt+B`).

4. **Install Missing Packages**
   - MiKTeX will prompt to install required packages if they are missing. Accept the prompt to download them.

---

## Additional Notes

- Ensure that the paths to Perl and MiKTeX binaries are added to your system's PATH environment variable for proper integration.
  - **Windows**: This is usually handled during installation, but you can verify it in System Properties > Advanced > Environment Variables.
  - **Linux**: Add the paths to your `~/.bashrc` or `~/.zshrc` file, e.g.:
    ```bash
    export PATH="$PATH:/path/to/perl/bin:/path/to/miktex/bin"
    ```

- For Linux users, consider alternatives like `TeX Live` if MiKTeX isn't supported in your distribution. Use the appropriate installation commands for your distribution.

---

Now you’re all set up to edit and compile LaTeX documents in Visual Studio Code with LaTeX Workshop. Happy TeXing!
