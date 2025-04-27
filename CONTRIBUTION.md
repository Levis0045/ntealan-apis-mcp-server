# Contributing

We welcome contributions! To get started:

1. **Fork the repository** and clone your fork.
2. **Create a new branch** for your feature or bugfix:
   ```bash
   git checkout -b my-feature
   ```
3. **Make your changes** with clear comments and docstrings.
4. **Add or update tests** as appropriate.
5. **Ensure code style** follows [PEP8](https://www.python.org/dev/peps/pep-0008/).
6. **Commit and push** your changes:
   ```bash
   git commit -am "Add my feature"
   git push origin my-feature
   ```
7. **Open a Pull Request** on GitHub with a clear description of your changes.

## Guidelines

- Write clear, concise docstrings for all public functions and classes.
- Add comments to explain non-obvious logic.
- Keep functions small and focused.
- Update the documentation if you add or change features.
- Be respectful and constructive in code reviews and discussions.


---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---


## Example: Registering New Resources

To add a new resource, define your async function in `src/ntealanapi_mcp/resources/` and register it in `main.py`:

```python
async def get_example_resource(param: str, ctx: Context) -> McpResourceResponse:
    """
    Example resource function.
    """
    # ...implementation...
    return {"status": "OK", "data": "example"}

ntl_mcp_server.add_resource_fn(
    lambda param: get_example_resource(param, ntl_mcp_server.get_context()),
    name="get_example_resource",
    uri="ntealan-apis://example/{param}",
    tags=["example-endpoint", "mcp-resource"],
    mime_type="application/json",
    description="Get example resource"
)
```

---

Happy contributing!

