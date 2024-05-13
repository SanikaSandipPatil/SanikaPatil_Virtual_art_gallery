# main/MainModule.py

from dao.crime_analysis_service_impl import CrimeAnalysisServiceImpl
from entity.artwork import Artwork
from entity.Artist import Artist
from entity.User import User
from entity.Gallery import Gallery
from dao.ivirtualartgallery import *

class MainModule:
    @staticmethod
    def get_artwork_details():
        title = input("Enter artwork title: ")
        description = input("Enter artwork description: ")
        creation_date = input("Enter artwork creation date: ")
        medium = input("Enter artwork medium: ")
        image_url = input("Enter artwork image URL: ")
        #return Artwork(title, description, creation_date, medium, image_url)
        artwork = Artwork()  # Create an instance of Artwork
        artwork.set_title(title)
        artwork.set_description(description)
        artwork.set_creation_date(creation_date)
        artwork.set_medium(medium)
        artwork.set_image_url(image_url)

        return artwork
    @staticmethod
    def get_artist_details():
        name = input("Enter artist name: ")
        biography = input("Enter artist biography: ")
        birth_date = input("Enter artist birth date: ")
        nationality = input("Enter artist nationality: ")
        website = input("Enter artist website: ")
        contact_info = input("Enter artist contact information: ")
        #return Artist(name, biography, birth_date, nationality, website, contact_info)
        artist = Artist()
        artist.set_name(name)
        artist.set_biography(biography)
        artist.set_birth_date(birth_date)
        artist.set_nationality(nationality)
        artist.set_website(website)
        artist.set_contact_info(contact_info)

        return artist
    @staticmethod
    def get_user_details():
        username = input("Enter username: ")
        password = input("Enter password: ")
        email = input("Enter email: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        date_of_birth = input("Enter date of birth: ")
        profile_picture = input("Enter profile picture URL: ")
        #return User(username, password, email, first_name, last_name, dob, profile_picture)
        user = User()
        user.set_username(username)
        user.set_password(password)
        user.set_email(email)
        user.set_first_name(first_name)
        user.set_last_name(last_name)
        user.set_date_of_birth(date_of_birth)
        user.set_profile_picture(profile_picture)

        return user



    @staticmethod
    def get_gallery_details():
        name = input("Enter gallery name: ")
        description = input("Enter gallery description: ")
        location = input("Enter gallery location: ")
        curator = input("Enter curator ID: ")
        opening_hours = input("Enter opening hours: ")
        #return Gallery(name, description, location, curator_id, opening_hours)
        gallery = Gallery()
        gallery.set_name(name)
        gallery.set_description(description)
        gallery.set_location(location)
        gallery.set_curator(curator)
        gallery.set_opening_hours(opening_hours)

        return gallery
    @staticmethod
    def main():
        # Create an instance of the service implementation
        crime_analysis_service = CrimeAnalysisServiceImpl()

        while True:
            # Display menu options
            print("\nMenu:")
            print("1. Add Artwork")
            print("2. Add Artist")
            print("3. Add User")
            print("4. Add Gallery")
            print("5. update record")
            print("6. delete record")
            print("7. get Artwork By Id")
            print("8. search Artworks")
            print("9. add Artwork To Favorite")
            print("10.remove Artwork From Favorite")
            print("11.  get User Favorite Artworks")
            print("12. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                artwork = MainModule.get_artwork_details()
                crime_analysis_service.add_artwork(artwork)

            elif choice == '2':
                artist = MainModule.get_artist_details()
                crime_analysis_service.add_artist(artist)

            elif choice == '3':
                user = MainModule.get_user_details()
                crime_analysis_service.add_user(user)

            elif choice == '4':
                gallery = MainModule.get_gallery_details()
                crime_analysis_service.add_gallery(gallery)
            elif choice == '5':
                while True:
                    print("\nUpdate Menu:")
                    print("a. Update Artwork")
                    print("b. Update Artist")
                    print("c. Update User")
                    print("d.Update Gallery")
                    # Other update options...
                    print("e. Return to main menu")

                    update_choice = input("Enter your update choice: ")

                    if update_choice == 'a':
                        # Update Artwork
                        artwork_id = input("Enter artwork ID to update: ")
                        artwork = crime_analysis_service.get_artwork_by_id(artwork_id)
                        if artwork:
                            print("Enter new details for the artwork:")
                            new_title = input("Enter new title: ")
                            new_description = input("Enter new description: ")
                            new_creation_date = input("Enter new creation date: ")
                            new_medium = input("Enter new medium: ")
                            new_image_url = input("Enter new image URL: ")

                            # Create a new Artwork instance with updated details
                            new_artwork = Artwork(artwork_id, new_title, new_description, new_creation_date, new_medium,
                                                  new_image_url)

                            # Update the artwork
                            crime_analysis_service.update_artwork(new_artwork)
                            print("Artwork updated successfully.")
                        else:
                            print("Artwork not found.")

                    elif update_choice == 'b':
                        # Update Artist
                        artist_id = input("Enter artist ID to update: ")
                        artist = crime_analysis_service.get_artist_by_id(artist_id)
                        if artist:
                            print("Enter new details for the artist:")
                            new_name = input("Enter new name: ")
                            new_biography = input("Enter new biography: ")
                            new_birth_date = input("Enter new birth date: ")
                            new_nationality = input("Enter new nationality: ")
                            new_website = input("Enter new website: ")
                            new_contact_info = input("Enter new contact info: ")

                            # Create a new Artist instance with updated details
                            updated_artist = Artist(artist_id, new_name, new_biography, new_birth_date, new_nationality,
                                                    new_website, new_contact_info)

                            # Update the artist
                            crime_analysis_service.update_artist(updated_artist)
                            print("Artist updated successfully.")
                        else:
                            print("Artist not found.")

                    elif update_choice == 'c':
                        # Update User
                        user_id = input("Enter user ID to update: ")
                        user = crime_analysis_service.get_user_by_id(user_id)
                        if user:
                            print("Enter new details for the user:")
                            new_username = input("Enter new username: ")
                            new_password = input("Enter new password: ")
                            new_email = input("Enter new email: ")
                            new_first_name = input("Enter new first name: ")
                            new_last_name = input("Enter new last name: ")
                            new_date_of_birth = input("Enter new date of birth: ")
                            new_profile_picture = input("Enter new profile picture URL: ")

                            # Create a new User instance with updated details
                            updated_user = User(user_id, new_username, new_password, new_email, new_first_name,
                                                new_last_name, new_date_of_birth, new_profile_picture)

                            # Update the user
                            crime_analysis_service.update_user(updated_user)
                            print("User updated successfully.")
                        else:
                            print("User not found.")

                    elif update_choice == 'd':
                        # Update Gallery
                        gallery_id = input("Enter gallery ID to update: ")
                        gallery = crime_analysis_service.get_gallery_by_id(gallery_id)
                        if gallery:
                            print("Enter new details for the gallery:")
                            new_name = input("Enter new name: ")
                            new_description = input("Enter new description: ")
                            new_location = input("Enter new location: ")
                            new_curator = input("Enter new curator: ")
                            new_opening_hours = input("Enter new opening hours: ")

                            # Create a new Gallery instance with updated details
                            updated_gallery = Gallery(gallery_id, new_name, new_description, new_location, new_curator,
                                                      new_opening_hours)

                            # Update the gallery
                            crime_analysis_service.update_gallery(updated_gallery)
                            print("Gallery updated successfully.")
                        else:
                            print("Gallery not found.")

            elif choice == '6':
                delete_choice = input(
                    "Choose entity to delete:\n1. Artwork\n2. Artist\n3. User\n4. Gallery\nEnter your choice: ")
                if delete_choice == '1':
                    artwork_id = input("Enter artwork ID to delete: ")
                    crime_analysis_service.delete_artwork(artwork_id)
                elif delete_choice == '2':
                      artist_id = input("Enter artist ID to delete: ")
                      crime_analysis_service.delete_artist(artist_id)
                elif delete_choice == '3':
                       user_id = input("Enter user ID to delete: ")
                       crime_analysis_service.delete_user(user_id)
                elif delete_choice == '4':
                        gallery_id = input("Enter gallery ID to delete: ")
                        crime_analysis_service.delete_gallery(gallery_id)
                else:
                  print("Invalid choice.")

            elif choice == '7':
                artwork_id = input("Enter artwork ID to retrieve: ")
                artwork = crime_analysis_service.get_artwork_by_id(artwork_id)
                if artwork:
                      print("Artwork found:")
                      print(artwork)
                else:
                      print("Artwork not found.")

            elif choice == '8':
                search_term = input("Enter search term: ")
                artworks = crime_analysis_service.search_artworks(search_term)
                if artworks:
                    print("Search results:")
                    for artwork in artworks:
                        print(artwork)
                else:
                    print("No artworks found matching the search term.")

            elif choice == '9':
                user_id = input("Enter your user ID: ")
                artwork_id = input("Enter artwork ID to add to favorites: ")
                success = crime_analysis_service.add_artwork_to_favorite(int(user_id), int(artwork_id))
                if success:
                    print("Artwork added to favorites successfully.")
                else:
                    print("Failed to add artwork to favorites.")

            elif choice == '10':
                user_id = input("Enter your user ID: ")
                artwork_id = input("Enter artwork ID to remove from favorites: ")
                success = crime_analysis_service.remove_artwork_from_favorite(int(user_id), int(artwork_id))
                if success:
                    print("Artwork removed from favorites successfully.")
                else:
                    print("Failed to remove artwork from favorites.")

            elif choice == '11':
                user_id = input("Enter user ID to retrieve favorite artworks: ")
                favorite_artworks = crime_analysis_service.get_user_favorite_artworks(int(user_id))
                if favorite_artworks:
                    print("User favorite artworks:")
                    for artwork in favorite_artworks:
                        print(artwork)
                else:
                    print("No favorite artworks found for the user.")

                # Other update options...
            elif choice == '12':
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Please select a valid option.")

# Call the main method when this script is executed
if __name__ == "__main__":
    MainModule.main()

