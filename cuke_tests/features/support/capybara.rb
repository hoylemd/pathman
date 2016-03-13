require 'minitest/reporters'
require 'capybara/cucumber'
require 'capybara/poltergeist'
require 'byebug'
require 'HTTParty'

Capybara.javascript_driver = :poltergeist
Capybara.default_driver = :poltergeist
Capybara.app_host = ENV['BASE_URL']

After do |scenario|
  if scenario.failed?
    path = "screenshots/debug_#{Time.now.to_i}.png"
    page.save_screenshot(path)
    embed path, 'image/png', 'SCREENSHOT'
  end
end
