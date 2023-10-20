import sqlite3

conn = sqlite3.connect("account.db")
c = conn.cursor()

# Create accounts table if it doesn't already exist
c.execute(
    """CREATE TABLE IF NOT EXISTS accounts (

          user text unique,
          pass text,
          first text,
          last text,
          university text,
          major text

          )"""
)

c.execute(
    """CREATE TABLE IF NOT EXISTS jobs (

          title text,
          description text,
          employer text,
          location text,
          salary text,
          first text,
          last text

          )"""
)

c.execute(
    """CREATE TABLE IF NOT EXISTS friends (
    
          user text unique,
          friend_user text unique

          )"""
)

c.execute(
    """CREATE TABLE IF NOT EXISTS friends_list (

          user text unique,
          friend_user text unique

          )"""
)

c.execute(
    """CREATE TABLE IF NOT EXISTS profile (

          user text unique,
          university text,
          major text,
          title text,
          about text

          )"""
)

c.execute(
    """CREATE TABLE IF NOT EXISTS experience (

          user text unique,
          experienceId text unique,
          title text,
          employer text,
          date_started text,
          date_ended text,
          location text,
          description text

          )"""
)

c.execute(
    """CREATE TABLE IF NOT EXISTS education (

          user text unique,
          educationId text unique,
          school_name text,
          degree text,
          years_attended text

          )"""
)


def create_profile(username, university, major, title, about):
    """Returns True if the profile was successfully created, False otherwise"""
    try:
        with conn:
            # Insert username, password, first name, and last name into database
            c.execute(
                "INSERT INTO profile VALUES (:user, :university, :major, :title, :about)",
                {
                    "user": username,
                    "university": university,
                    "major": major,
                    "title": title,
                    "about": about,
                },
            )
        return True
    except sqlite3.Error as error:
        print("Failed to add profile into sqlite table:", error)
        return False


def delete_profile(username):
    """Returns True if the profile was successfully deleted, False otherwise"""
    try:
        with conn:
            # Delete the profile with the provided username
            c.execute("DELETE FROM profile WHERE user = ?", (username,))
        return True
    except sqlite3.Error as error:
        print("Failed to delete profile from the sqlite table:", error)
        return False


def create_experience(
    user, experienceId, title, employer, date_started, date_ended, location, description
):
    """Returns True if the experience was successfully created, False otherwise"""
    try:
        with conn:
            # Insert username, password, first name, and last name into database
            c.execute(
                "INSERT INTO experience VALUES (:user, :experienceId, :title, :employer, :date_started, :date_ended, :location, :description)",
                {
                    "user": user,
                    "experienceId": experienceId,
                    "title": title,
                    "employer": employer,
                    "date_started": date_started,
                    "date_ended": date_ended,
                    "location": location,
                    "description": description,
                },
            )
        return True
    except sqlite3.Error as error:
        print("Failed to add experience into sqlite table:", error)
        return False


def delete_experience(user, experienceId):
    """Returns True if the experience was successfully deleted, False otherwise"""
    try:
        with conn:
            # Delete the experience with the provided username
            c.execute(
                "DELETE FROM experience WHERE user = ? AND experienceId = ?",
                (
                    user,
                    experienceId,
                ),
            )
        return True
    except sqlite3.Error as error:
        print("Failed to delete experience from the sqlite table:", error)
        return False


def create_education(user, educationId, school_name, degree, years_attended):
    """Returns True if the education was successfully created, False otherwise"""
    try:
        with conn:
            # Insert username, password, first name, and last name into database
            c.execute(
                "INSERT INTO education VALUES (:user, :educationId, :school_name, :degree, :years_attended)",
                {
                    "user": user,
                    "educationId": educationId,
                    "school_name": school_name,
                    "degree": degree,
                    "years_attended": years_attended,
                },
            )
        return True
    except sqlite3.Error as error:
        print("Failed to add education into sqlite table:", error)
        return False


def delete_education(user, educationId):
    """Returns True if the education was successfully deleted, False otherwise"""
    try:
        with conn:
            # Delete the education with the provided username
            c.execute(
                "DELETE FROM education WHERE user = ? AND educationId = ?",
                (
                    user,
                    educationId,
                ),
            )
        return True
    except sqlite3.Error as error:
        print("Failed to delete education from the sqlite table:", error)
        return False


def create_user(username, password, first, last, university, major):
    """Returns True if the user was successfully created, False otherwise"""
    try:
        with conn:
            # Insert username, password, first name, and last name into database
            c.execute(
                "INSERT INTO accounts VALUES (:user, :pass, :first, :last, :university, :major)",
                {
                    "user": username,
                    "pass": password,
                    "first": first,
                    "last": last,
                    "university": university,
                    "major": major,
                },
            )
        return True
    except sqlite3.Error as error:
        print("Failed to add user into sqlite table:", error)
        return False


def delete_user(username):
    """Returns True if the user was successfully deleted, False otherwise"""
    try:
        with conn:
            # Delete the user with the provided username
            c.execute("DELETE FROM accounts WHERE user = ?", (username,))
        return True
    except sqlite3.Error as error:
        print("Failed to delete user from the sqlite table:", error)
        return False


def does_username_exist(username):
    """Returns True if the username already exists in the database, False otherwise"""
    c.execute("SELECT * FROM accounts WHERE user=:user", {"user": username})
    user_entry = c.fetchone()
    return user_entry is not None


def create_job(title, description, employer, location, salary, first, last):
    """Returns True if the user was successfully created, False otherwise"""
    try:
        with conn:
            # Insert username, password, first name, and last name into database
            c.execute(
                "INSERT INTO jobs VALUES (:title, :description, :employer, :location,:salary, :first, :last)",
                {
                    "title": title,
                    "description": description,
                    "employer": employer,
                    "location": location,
                    "salary": salary,
                    "first": first,
                    "last": last,
                },
            )
        return True
    except sqlite3.Error as error:
        print("Failed to add job into sqlite table:", error)
        return False


def delete_job(title):
    """Returns True if the job was successfully deleted, False otherwise"""
    try:
        with conn:
            # Delete the job with the provided title
            c.execute("DELETE FROM jobs WHERE title = ?", (title,))
        return True
    except sqlite3.Error as error:
        print("Failed to delete job from the sqlite table:", error)
        return False


def add_friend(username, friend_username):
    """Returns True if the friend was successfully added into the database, False otherwise"""
    try:
        with conn:
            c.execute(
                "INSERT INTO friends VALUES (:user, :friend_user)",
                {"user": username, "friend_user": friend_username},
            )
        return True
    except sqlite3.Error as error:
        print("Failed to add friend to the sqlite table:", error)
        return False


def search_name(firstname, lastname):
    """Returns True if the username already exists in the database, False otherwise"""
    c.execute(
        "SELECT * FROM accounts WHERE first=:first AND last=:last",
        {"first": firstname, "last": lastname},
    )
    user_entry = c.fetchone()
    return user_entry is not None


def get_username_from_last_name(lastname):
    """Returns a list of usernames if found with the friend's last name in the database, an empty list otherwise"""
    c.execute("SELECT user FROM accounts WHERE last=:last", {"last": lastname})
    users = c.fetchall()
    if users:
        return [user[0] for user in users]
    else:
        return []


def get_username_from_university(university):
    """Returns a list of username if found with the friend's university in the database, an empty list otherwise"""
    c.execute(
        "SELECT user FROM accounts WHERE university=:university",
        {"university": university},
    )
    users = c.fetchall()
    if users:
        return [user[0] for user in users]
    else:
        return []


def get_username_from_major(major):
    """Returns a list of username if found with the friend's major in the database, an empty list otherwise"""
    c.execute("SELECT user FROM accounts WHERE major=:major", {"major": major})
    users = c.fetchall()
    if users:
        return [user[0] for user in users]
    else:
        return []


def get_first_name(username):
    """Returns True if the username already exists in the database, False otherwise"""
    c.execute("SELECT * FROM accounts WHERE user=:user", {"user": username})
    user_entry = c.fetchone()
    return user_entry[2]


def get_last_name(username):
    """Returns True if the username already exists in the database, False otherwise"""
    c.execute("SELECT * FROM accounts WHERE user=:user", {"user": username})
    user_entry = c.fetchone()
    return user_entry[3]


def check_login(username, password):
    """Returns True if the username and password match a user in the database, False otherwise"""
    c.execute(
        "SELECT * FROM accounts WHERE user=:user AND pass=:pass",
        {"user": username, "pass": password},
    )
    accEntry = c.fetchone()
    return accEntry is not None


def get_num_of_users():
    """Returns the number of users in the database"""
    c.execute("SELECT COUNT(*) FROM accounts")
    result = c.fetchone()
    if result:
        return result[0]  # Extract the count from the result
    else:
        return 0  # Return 0 if there are no users in the database


def get_num_of_jobs():
    """Returns the number of users in the database"""
    c.execute("SELECT COUNT(*) FROM jobs")
    result = c.fetchone()
    if result:
        return result[0]  # Extract the count from the result
    else:
        return 0  # Return 0 if there are no users in the database


def does_friend_request_match(username, friend_username):
    """Returns friend username if the username already exists in the friends, False otherwise"""
    c.execute(
        "SELECT * FROM friends WHERE user=:user AND friend_user=:friend_user",
        {"user": friend_username, "friend_user": username},
    )
    user_entry = c.fetchone()
    if user_entry:
        return True
    else:
        return False


def pending_friend_request_list(username):
    """Returns friend username if the username already exists in the friends, False otherwise"""
    c.execute(
        "SELECT * FROM friends WHERE friend_user=:friend_user",
        {"friend_user": username},
    )
    user_entry = c.fetchall()

    if user_entry:
        return user_entry
    else:
        return False


def add_to_friend_list(username, friend_username):
    """Returns True if the friend was successfully added into the database, False otherwise"""
    try:
        with conn:
            c.execute(
                "INSERT INTO friends_list VALUES (:user, :friend_user)",
                {"user": username, "friend_user": friend_username},
            )
            c.execute(
                "INSERT INTO friends_list VALUES (:user, :friend_user)",
                {"user": friend_username, "friend_user": username},
            )
        return True
    except sqlite3.Error as error:
        print("Failed to add friend to the sqlite table:", error)
        return False


def delete_friend_request(username, friend_username):
    """Returns True if the friend was successfully deleted, False otherwise"""
    try:
        with conn:
            # Delete the friend with the provided username
            c.execute(
                "DELETE FROM friends WHERE user = ? AND friend_user = ?",
                (
                    friend_username,
                    username,
                ),
            )
        return True
    except sqlite3.Error as error:
        print("Failed to delete user from the sqlite table:", error)
        return False


def list_of_friends(username):
    """Returns friend username if the username already exists in the friends, False otherwise"""
    c.execute("SELECT * FROM friends_list WHERE user=:user", {"user": username})
    user_entry = c.fetchall()

    if user_entry:
        return user_entry
    else:
        return False


def does_friend_match(username, friend_username):
    """Returns friend username if the username already exists in the friends, False otherwise"""
    c.execute(
        "SELECT * FROM friends_list WHERE user=:user AND friend_user=:friend_user",
        {"user": username, "friend_user": friend_username},
    )
    user_entry = c.fetchone()
    if user_entry:
        return True
    else:
        return False


def delete_friend_from_list(username, friend_username):
    """Returns True if the friend was successfully deleted, False otherwise"""
    try:
        with conn:
            # Delete the friend with the provided username
            c.execute(
                "DELETE FROM friends_list WHERE user = ? AND friend_user = ?",
                (
                    friend_username,
                    username,
                ),
            )
            c.execute(
                "DELETE FROM friends_list WHERE user = ? AND friend_user = ?",
                (
                    username,
                    friend_username,
                ),
            )
        return True
    except sqlite3.Error as error:
        print("Failed to delete user from the sqlite table:", error)
        return False
