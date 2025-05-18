import time
import os
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from git import Repo

class GitCommitObserver(FileSystemEventHandler):
    def __init__(self, git_path):
        self.repo_path = git_path.parent
        self.logs_head_file = os.path.join(git_path, "logs", "HEAD")
        self.last_commit_hash = self.get_last_commit_hash()

    def get_last_commit_hash(self):
        try:
            repo = Repo(self.repo_path)
            return repo.head.commit.hexsha
        except:
            return None

    def on_modified(self, event):
        if event.src_path == self.logs_head_file:
            time.sleep(0.5)
            new_commit_hash = self.get_last_commit_hash()
            if new_commit_hash != self.last_commit_hash:
                self.last_commit_hash = new_commit_hash
                self.show_commit_details(new_commit_hash)

    def show_commit_details(self, commit_hash):
        repo = Repo(self.repo_path)
        commit = repo.commit(commit_hash)
        print("\nNovo commit detectado:")
        print(f"Hash: {commit.hexsha}")
        print(f"Autor: {commit.author.name} <{commit.author.email}>")
        print(f"Data: {commit.committed_datetime}")
        print(f"Mensagem: {commit.message.strip()}")
        print("Arquivos alterados:")

        parent = commit.parents[0] if commit.parents else None
        diffs = commit.diff(parent, create_patch=True)

        for diff in diffs:
            change_type = diff.change_type.upper()
            file_path = diff.a_path if diff.a_path else diff.b_path
            print(f"[{change_type}] {file_path}")

def find_git_repo(start_path="."):
    path = Path(start_path).resolve()
    while path != path.parent:
        git_dir = path / ".git"
        if git_dir.is_dir():
            return git_dir
        path = path.parent
    return None

def start_observing(git_dir):
    event_handler = GitCommitObserver(git_dir)
    observer = Observer()
    observer.schedule(event_handler, path=os.path.join(git_dir, "logs"), recursive=False)
    observer.start()
    print(f"Observando commits pelo arquivo: {event_handler.logs_head_file}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    git_repo = find_git_repo()
    if git_repo:
        start_observing(git_repo)
    else:
        print("Nenhum repositório Git encontrado no caminho atual ou acima.")
