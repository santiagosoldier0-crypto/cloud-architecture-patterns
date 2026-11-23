"""Local routing model: spokes communicate through the central hub."""
ROUTES = {
    "spoke-a": {"spoke-b": "hub", "spoke-c": "hub"},
    "spoke-b": {"spoke-a": "hub", "spoke-c": "hub"},
    "spoke-c": {"spoke-a": "hub", "spoke-b": "hub"},
}


def route(source: str, destination: str) -> list[str]:
    if source == destination and source in ROUTES:
        return [source]
    if source not in ROUTES or destination not in ROUTES[source]:
        raise ValueError("unknown spoke")
    return [source, "hub", destination]


if __name__ == "__main__":
    for spoke in ROUTES:
        print(f"{spoke} -> spoke-c: {' -> '.join(route(spoke, 'spoke-c'))}")
