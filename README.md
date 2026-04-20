# Kibitzer

*Stockfish and an LLM, arguing about your chess, every Monday morning.*

> Status: early development. Increment 0 — tooling skeleton.

Pulls your chess.com games, runs Stockfish on every position, uses an LLM to explain the mistakes in plain English, emails you a weekly digest.

See [docs/scope.md](docs/scope.md) for architecture and roadmap.

## Development

```bash
make install
make test
make check
make fmt
make lint
make typecheck
make clean
```

## License

MIT — see [LICENSE](LICENSE).
