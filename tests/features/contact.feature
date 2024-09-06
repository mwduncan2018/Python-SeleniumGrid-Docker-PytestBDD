@contact
Feature: Contact

Scenario Outline: Duncan Safe Product Footer Text
	When the Contact page is viewed
	Then the footer text should include <footerText> within <seconds> seconds

	Examples:
	| footerText             | seconds |
	| (Duncan Safe Product!) | 10      |

Scenario Outline: GitHub link
	When the Contact page is viewed
	Then the GitHub link <gitHub> should be provided

	Examples:
	| gitHub                          |
	| https://github.com/mwduncan2018 |

Scenario Outline: Technical skills are displayed
	When the Contact page is viewed
	Then the following <skill> should be listed

	Examples:
	| skill                       |
	| Selenium                    |
	| Appium                      |
	| Playwright                  |
	| pytest-bdd                  |
	| SpecFlow                    |
	| Java Cucumber               |
	| Docker                      |
	| Docker Compose              |
	| C# MVC                      |
	| Jenkins                     |
	| Amazon Web Services         |