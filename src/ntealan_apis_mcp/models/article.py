from pydantic import BaseModel


class Article(BaseModel):
    """
    Represents an article entity with user association and notification flag.

    Attributes:
        user_id (int): The ID of the user associated with the article.
        notify (bool): Whether to notify the user about changes to the article.
    """

    user_id: int
    notify: bool = False  # Notification flag for the user


class Dictionary(BaseModel):
    """
    Represents a dictionary entity with user association and notification flag.

    Attributes:
        user_id (int): The ID of the user associated with the dictionary.
        notify (bool): Whether to notify the user about changes to the dictionary.
    """

    user_id: int
    notify: bool = False  # Notification flag for the user


class Metadata(BaseModel):
    """
    Represents metadata information with user association and notification flag.

    Attributes:
        user_id (int): The ID of the user associated with the metadata.
        notify (bool): Whether to notify the user about changes to the metadata.
    """

    user_id: int
    notify: bool = False  # Notification flag for the user


class Contribution(BaseModel):
    """
    Represents a contribution entity with user association and notification flag.

    Attributes:
        user_id (int): The ID of the user associated with the contribution.
        notify (bool): Whether to notify the user about changes to the contribution.
    """

    user_id: int
    notify: bool = False  # Notification flag for the user
