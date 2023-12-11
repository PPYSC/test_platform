import subprocess


class AbstractExecutable:
    def __init__(self, exe_path):
        self.exe_path = exe_path
        self.description = "This class is abstract, do not use!"

    def __repr__(self):
        return f"<executable: {self.__class__.__name__}, {self.description}>"

    def _run_cmd(self, cmd):
        return subprocess.run(cmd, capture_output=True, shell=True, encoding="utf8")

    def run(self, exe_input):
        completed_progress_list = []
        cmd = f"env GOTRACEBACK=crash {self.exe_path} < {exe_input}"
        completed_progress_list.append(self._run_cmd(cmd))
        return completed_progress_list


class CommonExecutable(AbstractExecutable):
    pass
