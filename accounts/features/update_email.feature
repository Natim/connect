Feature: Update Email

    Scenario: User views page
        Given I am an active authenticated user
        When I visit the update email page
        Then I see the update email form
        And the email field is prepopulated with my email ("active.user1@test.test")

    Scenario Outline: User submits invalid data to the update email form
        Given I am an active authenticated user
        When I visit the update email page
        And I input <email> into the email field
        And I input <password> into the password field
        And I submit the form
        Then I see <error>

        Examples:
            |   email                       |   password    |   error                                                               |
            |   ""                          |   "pass"      |   "This field is required."                                           |
            |   "invalidemail"              |   "pass"      |   "Please enter a valid email address."                               |
            |   "inactive.user2@test.test"  |   "pass"      |   "Sorry, this email address is already registered to another user."  |
            |   "a.new.email@test.test"     |   ""          |   "This field is required."                                           |
            |   "a.new.email@test.test"     |   "wrongpass" |   "Incorrect password. Please try again."                             |

    Scenario: User updates their email
        Given I am an active authenticated user
        When I visit the update email page
        When I input "a.new.email@test.test" into the email field
        And I input "pass" into the password field
        And I submit the form
        Then I see "Your Connect email has been updated."

