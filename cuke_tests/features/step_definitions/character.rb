When(/I enter a new character name$/) do
  @character_name = Faker::Name.name
  fill_in "Name", with: @character_name
end

# rolls dice. n dice, with s sides.
def nds(n,s)
  (0...(n)).map { rand(s) + 1 }.sort.reverse
end

def roll_nds(n, s)
  dice = nds n, s
  dice.reduce 0, :+
end

When(/I enter random hp into "(.*)"$/) do |label|
  hp = roll_nds 2, 6
  @hp = hp
  fill_in label, with: hp
end

Then(/I should see my hp$/) do
  hp_string = "#{@hp}hp"
  should_see hp_string
end

When(/I enter a random ability score into "(.*)"$/) do |label|
  score = nds(4, 6).slice(0, 3).reduce(0, :+)
  @ability_scores ||= {}
  @ability_scores[slugify label] = score
  fill_in label, with: score
end

Then(/I should see my (.*) score and mod$/) do |ability|
  byebug
end

Then(/I should see my character name$/) do
  should_see @character_name
end

When(/I click my character name$/) do
  click_on @character_name
end

When(/I choose "(.*)" as my race$/) do |race_name|
  @race = race_name
  choose_from_dropdown "Race", race_name
end

Then(/I should see my race$/) do
  should_see @race
end
