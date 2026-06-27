# Saucedemo Cart Tests

![Playwright Tests](https://github.com/raj2707/saucedemo-cart-tests/actions/workflows/playwright.yml/badge.svg)

Automated end-to-end shopping cart tests for saucedemo.com using Playwright + pytest,
structured with Page Object Model (POM).

## Tech stack
- Python 3.12
- Playwright (sync API)
- pytest + pytest-html
- GitHub Actions CI/CD (chromium, firefox, webkit)

## Test scenarios
- Happy path: add product, checkout, confirm order
- Multiple products in cart
- Remove product from cart
- Checkout with empty fields (validation)
- Product sorting (price low to high)

## Project structure
- pages/login_page.py       — Login Page Object
- pages/inventory_page.py   — Inventory Page Object
- pages/cart_page.py        — Cart Page Object
- pages/checkout_page.py    — Checkout Page Object
- tests/test_cart.py        — Test cases
- conftest.py               — Browser fixtures

## How to run
pip install -r requirements.txt
playwright install chromium
pytest tests/ -v

## CI/CD
Tests run automatically on every push via GitHub Actions across 3 browsers in parallel.
