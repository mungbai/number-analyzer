def main():
    from analyzer.cli import parse_arguments
    from analyzer.config_loader import load_config
    from analyzer.number_analyzer import NumberAnalyzer

    args = parse_arguments()
    config = load_config('analyzer-config.json')
    analyzer = NumberAnalyzer(config)
    analyzer.run(args.min, args.max)

if __name__ == "__main__":
    main()
