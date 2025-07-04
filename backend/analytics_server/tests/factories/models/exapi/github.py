from collections import namedtuple
from dataclasses import dataclass
from datetime import datetime
from typing import Dict

from mhq.exapi.models.github_timeline import GithubPullRequestTimelineEvents
from mhq.utils.time import time_now


def get_github_commit_dict(
    sha: str = "123456789098765",
    author_login: str = "author_abc",
    url: str = "https://github.com/123456789098765",
    message: str = "[abc 315] avoid mapping edit state",
    created_at: str = "2022-06-29T10:53:15Z",
) -> Dict:
    return {
        "sha": sha,
        "commit": {
            "committer": {"name": "abc", "email": "abc@midd.com", "date": created_at},
            "message": message,
        },
        "author": {
            "login": author_login,
            "id": 95607047,
            "node_id": "abc",
            "avatar_url": "",
        },
        "html_url": url,
    }


@dataclass
class GithubPullRequestReview:
    id: str
    submitted_at: datetime
    user_login: str

    @property
    def raw_data(self):
        return {
            "id": self.id,
            "submitted_at": self.submitted_at,
            "user": {
                "login": self.user_login,
            },
        }


def get_github_pull_request_review(
    review_id: str = "123456",
    submitted_at: datetime = time_now(),
    user_login: str = "abc",
) -> GithubPullRequestReview:

    return GithubPullRequestReview(review_id, submitted_at, user_login)


Branch = namedtuple("Branch", ["ref"])
User = namedtuple("User", ["login"])


@dataclass
class GithubPullRequest:
    number: int
    merged_at: datetime
    closed_at: datetime
    title: str
    html_url: str
    created_at: datetime
    updated_at: datetime
    base: Branch
    head: Branch
    user: User
    commits: int
    additions: int
    deletions: int
    changed_files: int
    merge_commit_sha: str

    @property
    def raw_data(self):
        return {
            "number": self.number,
            "merged_at": self.merged_at,
            "closed_at": self.closed_at,
            "title": self.title,
            "html_url": self.html_url,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "base": {"ref": self.base.ref},
            "head": {"ref": self.head.ref},
            "user": {"login": self.user.login},
            "commits": self.commits,
            "additions": self.additions,
            "deletions": self.deletions,
            "changed_files": self.changed_files,
            "requested_reviewers": [],
            "merge_commit_sha": self.merge_commit_sha,
        }


def get_github_pull_request(
    number: int = 1,
    merged_at: datetime = None,
    closed_at: datetime = None,
    title: str = "random_title",
    html_url: str = None,
    created_at: datetime = time_now(),
    updated_at: datetime = time_now(),
    base_ref: str = "main",
    head_ref: str = "feature",
    user_login: str = "abc",
    commits: int = 1,
    additions: int = 1,
    deletions: int = 1,
    changed_files: int = 1,
    merge_commit_sha: str = "123456",
) -> GithubPullRequest:
    return GithubPullRequest(
        number,
        merged_at,
        closed_at,
        title,
        html_url,
        created_at,
        updated_at,
        Branch(base_ref),
        Branch(head_ref),
        User(user_login),
        commits,
        additions,
        deletions,
        changed_files,
        merge_commit_sha,
    )


def get_github_workflow_run_dict(
    run_id: str = "123456",
    actor_login: str = "abc",
    head_branch: str = "feature",
    status: str = "completed",
    conclusion: str = "success",
    run_started_at: str = "2022-06-29T10:53:15Z",
    created_at: str = "2022-06-29T10:53:15Z",
    updated_at: str = "2022-06-29T10:53:15Z",
    html_url: str = "",
) -> Dict:
    return {
        "id": run_id,
        "actor": {"login": actor_login},
        "head_branch": head_branch,
        "status": status,
        "conclusion": conclusion,
        "run_started_at": run_started_at,
        "created_at": created_at,
        "updated_at": updated_at,
        "html_url": html_url,
    }


def get_github_pr_timeline_event(
    event_id: str = "123456",
    user_login: str = "abc",
    event_type: str = "reviewed",
    timestamp: datetime = None,
    raw_data: Dict = None,
) -> GithubPullRequestTimelineEvents:
    if timestamp is None:
        timestamp = time_now()

    if raw_data is None:
        raw_data = {
            "id": event_id,
            "user": {"login": user_login},
            "submitted_at": timestamp.isoformat(),
            "state": "approved",
        }

    return GithubPullRequestTimelineEvents(
        event_type=event_type,
        data=raw_data,
    )
