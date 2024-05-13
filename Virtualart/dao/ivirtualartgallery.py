from abc import ABC, abstractmethod
from typing import List
from entity.artwork import Artwork

class IVirtualArtGallery(ABC):
    @abstractmethod
    def add_artwork(self, artwork):
        pass

    @abstractmethod
    def update_artwork(self, artwork):
        pass

    @abstractmethod
    def delete_artwork(self, artwork_id):
        pass

    @abstractmethod
    def get_artwork_by_id(self, artwork_id: int) -> Artwork:
        pass

    @abstractmethod
    def search_artworks(self, search_term: str) -> List[Artwork]:
        pass

    @abstractmethod
    def add_artwork_to_favorite(self, user_id, artwork_id):
        pass

    @abstractmethod
    def remove_artwork_from_favorite(self, user_id: int, artwork_id: int) -> bool:
        pass

    @abstractmethod
    def get_user_favorite_artworks(self, user_id: int) -> List[Artwork]:
        pass

    @abstractmethod
    def update_artist(self, artist):
        pass

    @abstractmethod
    def get_artist_by_id(self, artist_id):
        pass

    @abstractmethod
    def update_user(self, user):
        pass

    @abstractmethod
    def get_user_by_id(self, user_id):
        pass

    @abstractmethod
    def delete_artist(self, artist_id):
        pass

    @abstractmethod
    def delete_user(self, user_id):
        pass

    @abstractmethod
    def delete_gallery(self, gallery_id):
        pass