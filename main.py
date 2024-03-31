from src import get_metro_products, refactor_products, save_data, STOCKS, check_data


def main() -> None:
    products = []
    for stock in STOCKS:
        products.extend(refactor_products(get_metro_products(stock)))
    print(check_data())


if __name__ == '__main__':
    main()
