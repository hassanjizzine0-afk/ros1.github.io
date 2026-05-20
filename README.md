markdown

```math
\int_{a}^{b} f(x) dx = F(b) - F(a)

text


That way GitHub properly recognizes the entire block as a mathematical expression.

---

## Quick summary of both working syntaxes on GitHub:

| Type | Syntax | Example |
|------|--------|---------|
| **Inline math** | `$...$` | `$E = mc^2$` |
| **Display math (inline block)** | `$$...$$` | `$$\int x^2 dx$$` |
| **Code block math** | ` ```math ... ``` ` | For multi-line or complex equations |

---

## Example using your integral:

**Code block style:**
```markdown
```math
\int_{a}^{b} f(x) dx = F(b) - F(a)

text


**Display math style:**
```markdown
$$
\int_{a}^{b} f(x) dx = F(b) - F(a)
$$
