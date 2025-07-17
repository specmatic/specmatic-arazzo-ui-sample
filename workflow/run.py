import pathlib
import os
import subprocess

ROOT_DIR = pathlib.Path(__file__).parent
MINIMAL_SPEC_FILE = "location_order_workflow.arazzo.yaml"
EXTRAPOLATED_SPEC_FILE = "./output/location_order_workflow.arazzo_extrapolated.arazzo.yaml"
HTML_REPORT = ROOT_DIR / "build" / "reports" / "specmatic" / "html" / "index.html"


def run_arazzo_command(name: str, command: list[str]):
    print(f"\n=== Running: {name} ===")
    final_command = " ".join([name, *command])
    expose = "--network host" if name != "validate" else "-p 3000:3000 -p 5000:5000"
    try:
        docker_command = f"docker run --rm {expose} -v {ROOT_DIR}:/usr/src/app specmatic/specmatic-arazzo:latest {final_command}"
        subprocess.run(docker_command, shell=True, check=True)  # noqa: S602
    except subprocess.CalledProcessError as e:
        print(f"Error: Command failed with exit code {e.returncode}")
    finally:
        print(f"=== Done: {name} ===\n")


def show_menu():
    print("===== Docker Command Menu =====")
    print("1. Extrapolate minimal Arazzo Specification")
    print("2. Validate Extrapolated Arazzo Specification")
    print("3. Run Arazzo Workflow Test")
    print("4. Start Arazzo Mock")
    print("5. Open Generated HTML Report")
    print("================================")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        match choice:
            case "1":
                run_arazzo_command("extrapolate", ["--spec-file", MINIMAL_SPEC_FILE])
            case "2":
                run_arazzo_command("validate", ["--spec-file", EXTRAPOLATED_SPEC_FILE])
            case "3":
                run_arazzo_command("test", [EXTRAPOLATED_SPEC_FILE, "--serverUrlIndex", "1"])
            case "4":
                run_arazzo_command("mock", ["--spec-file", EXTRAPOLATED_SPEC_FILE])
            case "5":
                os.startfile(str(HTML_REPORT))
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
