Feature: Characters

  Scenario: Home layout correctly
    When I visit the home page
    Then I should see "Welcome to Pathman!"
    And I should see "Character List"
    And I should see "Classes"
    And I should see "Races"

  Scenario: Character List layout
    When I visit the home page
    And I click "Character List"
    Then I should see "Characters"
    And I should see "Create New"

  Scenario: Races list layout
    When I visit the home page
    And I click "Races"
    Then I should see "Races"
    And I should see "Dwarf"
    And I should see "Elf"
    And I should see "Gnome"
    And I should see "Half-Elf"
    And I should see "Half-Orc"
    And I should see "Halfling"
    And I should see "Human"

   Scenario: Classes list layout
    When I visit the home page
    And I click "Classes"
    Then I should see "Classes"
    And I should see "Barbarian"
    And I should see "Bard"
    And I should see "Cleric"
    And I should see "Druid"
    And I should see "Fighter"
    And I should see "Monk"
    And I should see "Paladin"
    And I should see "Ranger"
    And I should see "Rogue"
    And I should see "Sorcerer"
    And I should see "Wizard"
