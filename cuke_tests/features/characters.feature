Feature: Characters

  Background:
    When I visit the home page

  Scenario: Home layout correctly
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

  Scenario: Create a new character
    When I visit the characters page
    And I click "Create New"
    Then I should see a "Create" button
    When I enter a new character name
    And I enter random hp into "Hp"
    And I choose "Human" as my race
    And I enter a random ability score into "Strength"
    And I enter a random ability score into "Dexterity"
    And I enter a random ability score into "Constitution"
    And I enter a random ability score into "Intelligence"
    And I enter a random ability score into "Wisdom"
    And I enter a random ability score into "Charisma"
    And I click "Create"
    Then I should see my character name
    When I click my character name
    Then I should see my character name
    And I should see my race
    And I should see my hp
    And I should see my Strength score and mod
    And I should see my Dexterity score and mod
    And I should see my Constitution score and mod
    And I should see my Intelligence score and mod
    And I should see my Wisdom score and mod
    And I should see my Charisma score and mod

