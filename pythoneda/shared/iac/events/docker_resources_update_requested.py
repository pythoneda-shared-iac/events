# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/events/docker_resources_update_requested.py

This file declares the DockerResourcesUpdateRequested event.

Copyright (C) 2024-today pythoneda-shared-iac/events

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from .abstract_docker_resources_event import AbstractDockerResourcesEvent
from typing import Dict, List


class DockerResourcesUpdateRequested(AbstractDockerResourcesEvent):
    """
    Represents the moment Dockerresources update is requested.

    Class name: DockerResourcesUpdateRequested

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(
        self,
        stackName: str,
        projectName: str,
        location: str,
        imageName: str,
        imageVersion: str,
        imageUrl: str = None,
        metadata: Dict = {},
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
    ):
        """
        Creates a new DockerResourcesUpdateRequested instance.
        :param stackName: The name of the stack.
        :type stackName: str
        :param projectName: The name of the project.
        :type projectName: str
        :param location: The location.
        :type location: str
        :param imageName: The name of the Docker image.
        :type imageName: str
        :param imageVersion: The version of the Docker image.
        :type imageVersion: str
        :param imageUrl: The url of the Docker image.
        :type imageUrl: str
        :param metadata: Additional request metadata.
        :type metadata: Dict
        :param previousEventIds: The id of previous events, if any.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        """
        super().__init__(
            stackName,
            projectName,
            location,
            imageName,
            imageVersion,
            imageUrl,
            metadata,
            previousEventIds,
            reconstructedId,
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
