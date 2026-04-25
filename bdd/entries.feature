Feature: Entry Management

Scenario Outline: Add new entry
  Given a entry list
  Given a entry with <firstname>, <lastname>, <address>, <phone_home> and <email>
  When I add the entry to the list
  Then the new entry list is equal to the old list with added entry

  Examples:
  | firstname  | lastname  | address  | phone_home  | email  |
  | firstname1 | lastname1 | address1 | phone_home1 | email1 |
  | firstname2 | lastname2 | address2 | phone_home2 | email2 |

Scenario Outline: Edit a entry
  Given a non-empty entry list
  Given a random entry from the list
  Given a entry with <firstname>, <lastname>, <address>, <phone_home> and <email>
  When I edit the entry in the list
  Then the new entry list is equal to the old list with edited entry

  Examples:
  | firstname  | lastname  | address  | phone_home  | email  |
  | firstname3 | lastname3 | address3 | phone_home3 | email3 |
  | firstname4 | lastname4 | address4 | phone_home4 | email4 |

Scenario: Delete a entry
  Given a non-empty entry list
  Given a random entry from the list
  When I delete the entry from the list
  Then the new entry list is equal to the old list without deleted entry