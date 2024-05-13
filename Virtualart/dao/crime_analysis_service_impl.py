'''from dao.ivirtualartgallery import IVirtualArtGallery
from util.db_connection import DBConnection
from entity.artwork import Artwork
from entity.User import User

class CrimeAnalysisServiceImpl:
    def __init__(self):
        self.connection = DBConnection.get_connection()

    def add_artwork(self, artwork):
        try:
            cursor = self.connection.cursor()
            # Prepare SQL query to insert artwork details
            sql_query = "INSERT INTO artwork (title, description, creation_date, medium, image_url) VALUES (%s, %s, %s, %s, %s)"
            # Execute SQL query
            cursor.execute(sql_query, (artwork.title, artwork.description, artwork.creation_date, artwork.medium, artwork.image_url))
            # Commit changes
            self.connection.commit()
            print("Artwork added successfully.")
        except Exception as e:
            print("Error adding artwork:", e)
            # Rollback changes if an error occurs
            self.connection.rollback()
        finally:
            # Close cursor
            cursor.close()


    def update_artwork(self, artwork):
        connection = self.db_conn_util.get_connection()
        try:
            cursor = connection.cursor()
            sql = "UPDATE Artwork SET Title = %s, Description = %s, CreationDate = %s, Medium = %s, ImageURL = %s WHERE ArtworkID = %s"
            values = (artwork.title, artwork.description, artwork.creation_date, artwork.medium, artwork.image_url, artwork.artwork_id)
            cursor.execute(sql, values)
            connection.commit()
            return True
        except Exception as e:
            print("Error updating artwork:", e)
            connection.rollback()
            return False
        finally:
            cursor.close()
            connection.close()

    def remove_artwork(self, artwork_id):
        connection = self.db_conn_util.get_connection()
        try:
            cursor = connection.cursor()
            sql = "DELETE FROM Artwork WHERE ArtworkID = %s"
            cursor.execute(sql, (artwork_id,))
            connection.commit()
            return True
        except Exception as e:
            print("Error removing artwork:", e)
            connection.rollback()
            return False
        finally:
            cursor.close()
            connection.close()

    def get_artwork_by_id(self, artwork_id):
        connection = self.db_conn_util.get_connection()
        try:
            cursor = connection.cursor(dictionary=True)
            sql = "SELECT * FROM Artwork WHERE ArtworkID = %s"
            cursor.execute(sql, (artwork_id,))
            artwork_data = cursor.fetchone()
            if artwork_data:
                artwork = Artwork(artwork_data['ArtworkID'], artwork_data['Title'], artwork_data['Description'],
                                  artwork_data['CreationDate'], artwork_data['Medium'], artwork_data['ImageURL'])
                return artwork
            else:
                return None
        except Exception as e:
            print("Error getting artwork by ID:", e)
            return None
        finally:
            cursor.close()
            connection.close()

    def search_artworks(self, keyword):
        connection = self.db_conn_util.get_connection()
        try:
            cursor = connection.cursor(dictionary=True)
            sql = "SELECT * FROM Artwork WHERE Title LIKE %s OR Description LIKE %s"
            cursor.execute(sql, ('%' + keyword + '%', '%' + keyword + '%'))
            artworks_data = cursor.fetchall()
            artworks = []
            for artwork_data in artworks_data:
                artwork = Artwork(artwork_data['ArtworkID'], artwork_data['Title'], artwork_data['Description'],
                                  artwork_data['CreationDate'], artwork_data['Medium'], artwork_data['ImageURL'])
                artworks.append(artwork)
            return artworks
        except Exception as e:
            print("Error searching artworks:", e)
            return []
        finally:
            cursor.close()
            connection.close()

    def add_artwork_to_favorite(self, user_id, artwork_id):
        connection = self.db_conn_util.get_connection()
        try:
            cursor = connection.cursor()
            sql = "INSERT INTO User_Favorite_Artwork (UserID, ArtworkID) VALUES (%s, %s)"
            cursor.execute(sql, (user_id, artwork_id))
            connection.commit()
            return True
        except Exception as e:
            print("Error adding artwork to favorites:", e)
            connection.rollback()
            return False
        finally:
            cursor.close()
            connection.close()

    def remove_artwork_from_favorite(self, user_id, artwork_id):
        connection = self.db_conn_util.get_connection()
        try:
            cursor = connection.cursor()
            sql = "DELETE FROM User_Favorite_Artwork WHERE UserID = %s AND ArtworkID = %s"
            cursor.execute(sql, (user_id, artwork_id))
            connection.commit()
            return True
        except Exception as e:
            print("Error removing artwork from favorites:", e)
            connection.rollback()
            return False
        finally:
            cursor.close()
            connection.close()

    def get_user_favorite_artworks(self, user_id):
        connection = self.db_conn_util.get_connection()
        try:
            cursor = connection.cursor(dictionary=True)
            sql = "SELECT a.* FROM Artwork a JOIN User_Favorite_Artwork ufa ON a.ArtworkID = ufa.ArtworkID WHERE ufa.UserID = %s"
            cursor.execute(sql, (user_id,))
            artworks_data = cursor.fetchall()
            artworks = []
            for artwork_data in artworks_data:
                artwork = Artwork(artwork_data['ArtworkID'], artwork_data['Title'], artwork_data['Description'],
                                  artwork_data['CreationDate'], artwork_data['Medium'], artwork_data['ImageURL'])
                artworks.append(artwork)
            return artworks
        except Exception as e:
            print("Error getting user's favorite artworks:", e)
            return []
        finally:
            cursor.close()
            connection.close()
'''
# dao/CrimeAnalysisServiceImpl.py

from util.db_connection import DBConnection
from entity.artwork import Artwork
from entity.Artist import Artist
from entity.User import User
from entity.Gallery import Gallery
from typing import List
from exception.user_exceptions import UserException
from exception.user_exceptions import DateFormatException
import datetime

class CrimeAnalysisServiceImpl:
    connection = None

    def __init__(self):
        # Assign connection using DBConnection.get_connection() method
        self.connection = DBConnection.get_connection()

    # Other methods...

    # Artwork Management
    def add_artwork(self, artwork):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Artwork (title, description, creation_date, medium, image_url) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (artwork.get_title(), artwork.get_description(), artwork.get_creation_date(), artwork.get_medium(), artwork.get_image_url()))
            self.connection.commit()
            print("Artwork added successfully.")
            return True
        except Exception as e:
            print("Error adding artwork:", e)
            self.connection.rollback()
            return False
        finally:
            cursor.close()
# Artist Management
    def add_artist(self, artist):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Artist (name, biography, birth_date, nationality, website, contact_info) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (artist.get_name(), artist.get_biography(), artist.get_birth_date(), artist.get_nationality(), artist.get_website(), artist.get_contact_info()))
            self.connection.commit()
            print("Artist added successfully.")
        except Exception as e:
            print("Error adding artist:", e)
            self.connection.rollback()
        finally:
            cursor.close()
# User Management
    def add_user(self, user):
        cursor = None
        try:

            # Password validation
            password = user.get_password()
            if not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(
                    char in "!@#$%^&*()-_+=" for char in password):
                raise UserException(
                    "Password must contain at least 1 uppercase letter, 1 lowercase letter, and 1 special character")

            # Email validation
            email = user.get_email()
            if not email.endswith('@gmail.com'):
                raise UserException("Email must end with @gmail.com")

            date_of_birth = user.get_date_of_birth()
            try:
                datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')
            except ValueError:
                raise DateFormatException("Date format must be YYYY-MM-DD")


            cursor = self.connection.cursor()
            query = "INSERT INTO User (username, password, email, first_name, last_name, date_of_birth, profile_picture) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (user.get_username(), user.get_password(), user.get_email(), user.get_first_name(), user.get_last_name(), user.get_date_of_birth(), user.get_profile_picture()))
            self.connection.commit()
            print("User added successfully.")
        except (UserException, DateFormatException, Exception) as e:
            print("Error adding user:", e)
            self.connection.rollback()

        finally:
            if cursor:
             cursor.close()

# Gallery Management
    def add_gallery(self, gallery):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Gallery (name, description, location, curator, opening_hours) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (gallery.get_name(), gallery.get_description(), gallery.get_location(), gallery.get_curator(), gallery.get_opening_hours()))
            self.connection.commit()
            print("Gallery added successfully.")
            return True
        except Exception as e:
            print("Error adding gallery:", e)
            self.connection.rollback()
            return False
        finally:
            cursor.close()

 # Update Artwork
    def update_artwork(self, artwork):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE Artwork SET Title = %s, Description = %s, Creation_date = %s, Medium = %s, Image_url = %s WHERE artwork_id = %s"
            cursor.execute(query, (artwork.get_title(), artwork.get_description(), artwork.get_creation_date(), artwork.get_medium(), artwork.get_image_url(), artwork.get_artwork_id()))
            self.connection.commit()
            print("Artwork updated successfully.")
            return True
        except Exception as e:
            print("Error updating artwork:", e)
            self.connection.rollback()
            return False
        finally:
            cursor.close()
# Get Artwork by ID
    def get_artwork_by_id(self, artwork_id):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Artwork WHERE artwork_id = %s"
            cursor.execute(query, (artwork_id,))
            artwork_data = cursor.fetchone()
            if artwork_data:
                # Extract artwork details from the database query result
                artwork = Artwork(artwork_data[0], artwork_data[1], artwork_data[2], artwork_data[3], artwork_data[4], artwork_data[5])
                return artwork
            else:
                return None
        except Exception as e:
            print("Error fetching artwork by ID:", e)
        finally:
            cursor.close()

    def get_artist_by_id(self, artist_id):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Artist WHERE ArtistID = %s"
            cursor.execute(query, (artist_id,))
            artist_data = cursor.fetchone()
            if artist_data:
                # Extract artist details from the database query result
                artist = Artist(artist_data[0], artist_data[1], artist_data[2], artist_data[3], artist_data[4],
                                artist_data[5], artist_data[6])
                return artist
            else:
                return None
        except Exception as e:
            print("Error fetching artist by ID:", e)
        finally:
            cursor.close()

    def update_artist(self, artist):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE Artist SET name = %s, biography = %s, birth_date = %s, nationality = %s, website = %s, contact_info = %s WHERE ArtistID = %s"
            cursor.execute(query, (
            artist.get_name(), artist.get_biography(), artist.get_birth_date(), artist.get_nationality(),
            artist.get_website(), artist.get_contact_info(), artist.get_artist_id()))
            self.connection.commit()
            print("Artist updated successfully.")
        except Exception as e:
            print("Error updating artist:", e)
            self.connection.rollback()
        finally:
            cursor.close()

    def get_user_by_id(self, user_id):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM User WHERE UserID = %s"
            cursor.execute(query, (user_id,))
            user_data = cursor.fetchone()
            if user_data:
                # Extract user details from the database query result
                user = User(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4], user_data[5],
                            user_data[6], user_data[7])
                return user
            else:
                return None
        except Exception as e:
            print("Error fetching user by ID:", e)
        finally:
            cursor.close()

    def update_user(self, user):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE User SET username = %s, password = %s, email = %s, first_name = %s, last_name = %s, date_of_birth = %s, profile_picture = %s WHERE UserID = %s"
            cursor.execute(query, (
            user.get_username(), user.get_password(), user.get_email(), user.get_first_name(), user.get_last_name(),
            user.get_date_of_birth(), user.get_profile_picture(), user.get_user_id()))
            self.connection.commit()
            print("User updated successfully.")
        except Exception as e:
            print("Error updating user:", e)
            self.connection.rollback()
        finally:
            cursor.close()

    def get_gallery_by_id(self, gallery_id):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Gallery WHERE GalleryID = %s"
            cursor.execute(query, (gallery_id,))
            gallery_data = cursor.fetchone()
            if gallery_data:
                # Extract gallery details from the database query result
                gallery = Gallery(gallery_data[0], gallery_data[1], gallery_data[2], gallery_data[3], gallery_data[4],
                                  gallery_data[5])
                return gallery
            else:
                return None
        except Exception as e:
            print("Error fetching gallery by ID:", e)
        finally:
            cursor.close()

    def update_gallery(self, gallery):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE Gallery SET name = %s, description = %s, location = %s, curator = %s, opening_hours = %s WHERE GalleryID = %s"
            cursor.execute(query, (
            gallery.get_name(), gallery.get_description(), gallery.get_location(), gallery.get_curator(),
            gallery.get_opening_hours(), gallery.get_gallery_id()))
            self.connection.commit()
            print("Gallery updated successfully.")
            return True
        except Exception as e:
            print("Error updating gallery:", e)
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def delete_artwork(self, artwork_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Artwork WHERE artwork_id = %s"
            cursor.execute(query, (artwork_id,))
            self.connection.commit()
            print("Artwork deleted successfully.")
            return True
        except Exception as e:
            print("Error deleting artwork:", e)
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def delete_artist(self, artist_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Artist WHERE ArtistID = %s"
            cursor.execute(query, (artist_id,))
            self.connection.commit()
            print("Artist deleted successfully.")
        except Exception as e:
            print("Error deleting artist:", e)
            self.connection.rollback()
        finally:
            cursor.close()

    def delete_user(self, user_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM User WHERE UserID = %s"
            cursor.execute(query, (user_id,))
            self.connection.commit()
            print("User deleted successfully.")
        except Exception as e:
            print("Error deleting user:", e)
            self.connection.rollback()
        finally:
            cursor.close()

    def delete_gallery(self, gallery_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Gallery WHERE GalleryID = %s"
            cursor.execute(query, (gallery_id,))
            self.connection.commit()
            print("Gallery deleted successfully.")
            return True
        except Exception as e:
            print("Error deleting gallery:", e)
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def get_artwork_by_id(self, artwork_id: int) -> Artwork:
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM Artwork WHERE artwork_id = %s"  # Adjusted field name here
            cursor.execute(query, (artwork_id,))
            artwork_data = cursor.fetchone()
            if artwork_data:
                artwork = Artwork(
                    artwork_data['artwork_id'],  # Adjusted field name here
                    artwork_data['Title'],
                    artwork_data['Description'],
                    artwork_data['Creation_date'],
                    artwork_data['Medium'],
                    artwork_data['Image_url']
                )
                return artwork
            else:
                print("Artwork not found.")
                return None
        except Exception as e:
            print("Error retrieving artwork:", e)
            return None
        finally:
            cursor.close()

    def search_artworks(self, search_term: str) -> List[Artwork]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM Artwork WHERE Title LIKE %s OR Medium LIKE %s"
            cursor.execute(query, (f"%{search_term}%", f"%{search_term}%"))
            artworks_data = cursor.fetchall()
            artworks = []
            for artwork_data in artworks_data:
                artwork = Artwork(
                    artwork_data['artwork_id'],
                    artwork_data['Title'],
                    artwork_data['Description'],
                    artwork_data['Creation_date'],
                    artwork_data['Medium'],
                    artwork_data['Image_url']
                )
                artworks.append(artwork)
            return artworks
        except Exception as e:
            print("Error searching artworks:", e)
            return []
        finally:
            cursor.close()

    def add_artwork_to_favorite(self, user_id: int, artwork_id: int) -> bool:
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO User_Favorite_Artwork (UserID, artwork_id) VALUES (%s, %s)"
            cursor.execute(query, (user_id, artwork_id))
            self.connection.commit()
            return True
        except Exception as e:
            print("Error adding artwork to favorites:", e)
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def remove_artwork_from_favorite(self, user_id: int, artwork_id: int) -> bool:
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM User_Favorite_Artwork WHERE UserID = %s AND artwork_id = %s"
            cursor.execute(query, (user_id, artwork_id))
            self.connection.commit()
            return True
        except Exception as e:
            print("Error removing artwork from favorites:", e)
            return False
        finally:
            cursor.close()

    def get_user_favorite_artworks(self, user_id: int) -> List[Artwork]:
        try:
            cursor = self.connection.cursor()
            query = "SELECT a.* FROM artwork a JOIN User_Favorite_Artwork uf ON a.artwork_id = uf.artwork_id WHERE uf.UserID = %s"
            cursor.execute(query, (user_id,))
            artworks = []
            for row in cursor.fetchall():
                artwork = Artwork(*row)  # Assuming Artwork constructor matches database row structure
                artworks.append(artwork)
            return artworks
        except Exception as e:
            print("Error fetching user favorite artworks:", e)
            return []
        finally:
            cursor.close()


