import basico


def main():
    model = basico.load_biomodel("BIOMD0000000537")
    # Get and print the model name
    model_name = basico.model_info.get_model_name(model=model)
    print(model_name)


if __name__ == "__main__":
    main()
