from pygithub3.services.base import Service, MimeTypeMixin


class Comments(Service, MimeTypeMixin):
    """Consume `Review Comments API
    <http://developer.github.com/v3/pulls/comments/>`_

    """

    def list(self, number, user=None, repo=None):
        """List all the comments for a pull request

        :param str number: The number of the pull request
        :param str user: Username
        :param str repo: Repository

        """
        return self._get_result(
            self.make_request('pull_requests.comments.list', number=number,
                              user=user, repo=repo)
        )

    def get(self, number, user=None, repo=None):
        """Get a single comment

        :param str number: The comment to get
        :param str user: Username
        :param str repo: Repository

        """
        return self._get(
            self.make_request('pull_requests.comments.get', number=number,
                              user=user, repo=repo)
        )

    def create(self, number, body, user=None, repo=None):
        """Create a comment

        :param str number: the pull request to comment on
        :param str user: Username
        :param str repo: Repository

        """
        return self._post(
            self.make_request('pull_requests.comments.create', number=number,
                              body=body, user=user, repo=repo)
        )

    def edit(self, number, body, user=None, repo=None):
        """Edit a comment

        :param str number: The id of the comment to edit
        :param str user: Username
        :param str repo: Repository

        """
        return self._patch(
            self.make_request('pull_requests.comments.edit', number=number,
                              body=body, user=user, repo=repo)
        )

    def delete(self, number, user=None, repo=None):
        """Delete a comment

        :param str number: The comment to delete
        :param str user: Username
        :param str repo: Repository

        """
        return self._delete(
            self.make_request('pull_requests.comments.delete', number=number,
                              user=user, repo=repo)
        )
