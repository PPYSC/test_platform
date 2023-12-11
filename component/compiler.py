import subprocess


class AbstractCompiler:
    def __init__(self, go_path, compiler_path, description):
        self.go_path = go_path
        self.compiler_path = compiler_path
        self.description = "This class is abstract, do not use!"

    def __repr__(self):
        return f"<compiler: {self.__class__.__name__}, {self.description}>"

    def _run_cmd(self, cmd):
        return subprocess.run(cmd, capture_output=True, shell=True, encoding="utf8")

    def compile(self, project_path, project_name):
        completed_progress_list = []
        cmd = f"cd {project_path} && {self.go_path} mod init {project_name}"
        completed_progress_list.append(self._run_cmd(cmd))
        cmd = f"cd {project_path} && env GOTRACEBACK=crash {self.go_path} build -o {project_name}"
        completed_progress_list.append(self._run_cmd(cmd))
        return completed_progress_list


class GcOptOn(AbstractCompiler):
    def compile(self, project_path, project_name):
        compile_progress_list = []
        cmd = f"cd {project_path} && {self.go_path} mod init {project_name}"
        compile_progress_list.append(self._run_cmd(cmd))
        cmd = f"cd {project_path} && env GOTRACEBACK=crash {self.go_path} build -o {project_name}"
        compile_progress_list.append(self._run_cmd(cmd))
        return compile_progress_list


class GccgoOpt3(AbstractCompiler):
    def compile(self, project_path, project_name):
        compile_progress_list = []
        cmd = f"cd {project_path} && {self.go_path} mod init {project_name}"
        compile_progress_list.append(self._run_cmd(cmd))
        cmd = f"cd {project_path} && env GOTRACEBACK=crash {self.go_path} build -compiler={self.compiler_path} -gccgoflags='-O3' -o {project_name}"
        compile_progress_list.append(self._run_cmd(cmd))
        return compile_progress_list

