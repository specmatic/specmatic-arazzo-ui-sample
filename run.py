import pathlib
import platform
import signal
import subprocess
import sys

BACKEND_DIR = pathlib.Path(__file__).parent / "backend"
FRONTEND_DIR = pathlib.Path(__file__).parent / "frontend"
VENV_DIR = BACKEND_DIR / "venv"
REQUIREMENTS = BACKEND_DIR / "requirements.txt"


def venv_python():
    if platform.system() == "Windows":
        return VENV_DIR / "Scripts" / "python.exe"
    else:
        return VENV_DIR / "bin" / "python"


def ensure_venv():
    if not VENV_DIR.exists():
        print("Creating Python virtual environment...")
        subprocess.check_call([sys.executable, "-m", "venv", str(VENV_DIR)])  # noqa: S603

    if REQUIREMENTS.exists():
        print("Installing Python requirements...")
        subprocess.check_call([str(venv_python()), "-m", "pip", "install", "-r", str(REQUIREMENTS)])  # noqa: S603


def ensure_frontend_deps():
    print("Installing frontend dependencies...")
    npm_cmd = "npm.cmd" if platform.system() == "Windows" else "npm"
    subprocess.check_call([npm_cmd, "install"], cwd=str(FRONTEND_DIR))  # noqa: S603, S607


def run_backend():
    print("Starting backend...")
    return subprocess.Popen([str(venv_python()), "run.py"], cwd=str(BACKEND_DIR))  # noqa: S603


def run_frontend():
    print("Starting frontend...")
    npm_cmd = "npm.cmd" if platform.system() == "Windows" else "npm"
    return subprocess.Popen([npm_cmd, "run", "dev", "--", "--open"], cwd=str(FRONTEND_DIR), shell=False)  # noqa: S603


def main():
    ensure_venv()
    ensure_frontend_deps()
    backend_proc = run_backend()
    frontend_proc = run_frontend()

    def cleanup(*args):
        print("Terminating processes...")
        backend_proc.terminate()
        frontend_proc.terminate()
        sys.exit(0)

    signal.signal(signal.SIGINT, cleanup)
    signal.signal(signal.SIGTERM, cleanup)

    backend_proc.wait()
    frontend_proc.wait()


if __name__ == "__main__":
    main()
