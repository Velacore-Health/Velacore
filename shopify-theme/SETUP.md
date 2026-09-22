# Velacore Health — Shopify theme setup guide

This folder is a complete Shopify theme (the storefront design). The design, homepage,
product page, cart, and legal-page templates are all built. What's left is the **Shopify-admin
configuration** — the parts that can't live in theme code: products, subscription billing, the
EasyPay Direct gateway, pages, and navigation.

Work top to bottom. Nothing here requires a developer.

---

## 1. Upload the theme

1. Zip the **contents** of the `shopify-theme/` folder (the `assets`, `config`, `layout`,
   `locales`, `sections`, `snippets`, `templates` folders must be at the **top level** of the zip
   — not nested inside another folder). A ready-made `velacore-shopify-theme.zip` is included at the
   repo root.
2. Shopify admin → **Online Store → Themes → Add theme → Upload zip file**.
3. Click **Customize** to preview. Don't hit **Publish** until steps 2–7 are done (keep the store
   in password-protected "coming soon" mode while you finish).

---

## 2. Create your 5 program products

Products → **Add product**. Create one for each treatment. Model each as a **program that includes
the consultation** (this is the arsynl / LegitScript-safe pattern — you're selling the program +
physician review, not a drug off a shelf).

| Product title | Tag (drives filter + category) | Price |
|---|---|---|
| Tirzepatide Monthly Program | `weight` | from $349 |
| Semaglutide Monthly Program | `weight` | from $299 |
| NAD+ Program | `vitality` | $279 |
| Glutathione Monthly Program | `vitality` | $199 |
| Sermorelin Program | `hormone` | $329 |

For each product:
- **Media:** upload the vial image (the matching `.webp` files are in `assets/`, or use your own).
- **Tag:** add exactly one of `weight`, `vitality`, or `hormone` (the homepage filter + the product
  page category badge read this).
- **Description:** factual and mechanistic — no efficacy/outcome claims. (See the compliance notes.)
- **Variants (optional):** if a treatment has dose/supply options (e.g. 70-day vs 58-day), add them
  as variants — the product page renders them as selectable pills.
- **Short mechanism line (optional but nice):** add a metafield `custom.mechanism` (single-line
  text) like "Dual GIP / GLP-1 receptor agonist." It shows under the product title and on the card.
- **This is a physical product** that requires shipping. Leave "charge tax" per your accountant's
  guidance.

### Create the "Treatments" collection
Products → **Collections → Create collection** → name it **Treatments** → add all 5 products.
Then in the theme customizer, open the **Treatments** section and select this collection. (Until you
do, the homepage shows sample cards.)

---

## 3. Turn on subscriptions (monthly programs)

Shopify's native checkout supports subscriptions only through a **subscription app**. Install one:
- **Shopify Subscriptions** (free, first-party) — simplest, or
- **Recharge** / **Seal Subscriptions** — more features.

Then, on each monthly product, create a **monthly selling plan** ("Delivered every month"). The
product page automatically renders the selling-plan options when they exist. NAD+/Sermorelin can
stay one-time if you sell them as fixed-supply.

> ⚠️ Your payment processor must support the subscription app you pick. **Confirm with EasyPay
> Direct that their gateway works with your chosen subscription app before you commit** — some
> subscription apps only tokenize through specific gateways.

---

## 4. Connect EasyPay Direct (the payment gateway)

Shopify Payments will **not** approve peptides/Rx — you must use EasyPay's high-risk gateway.

1. Get your EasyPay Direct merchant account approved (this is where your **LegitScript certification**
   is required — see the compliance file).
2. Ask your EasyPay rep for their **Shopify integration** details. They typically provide a gateway
   that connects as a **third-party provider** under Settings → Payments → *Add payment methods →
   Choose a third-party provider*. (EasyPay commonly routes through NMI / Authorize.net-compatible
   gateways — use whichever they give you.)
3. In Shopify: **Settings → Payments** → add their gateway → enter the credentials EasyPay provides.
4. Place a **test order** end-to-end before going live.

---

## 5. The $20 physician fee

The customer pays the program price **+ a one-time $20 physician fee**, shipping included. Two ways
to add the fee (pick one):

- **(Recommended) Cart/checkout add-on:** use a small app or Shopify Function that adds a mandatory
  "$20 physician consultation fee" line at checkout. Search the Shopify App Store for "mandatory fee"
  / "surcharge," or have EasyPay/your dev add a Checkout Function.
- **(Simplest) Bake it in:** build the $20 into the program price and state clearly that pricing
  includes the physician fee. (The legal/refund pages already treat the $20 as separately
  identifiable and non-refundable, so the add-on approach maps more cleanly to the refund policy.)

Either way, make sure the **refund rule matches**: program payment refundable if not approved, the
**$20 physician fee is non-refundable**, medications non-returnable once dispensed.

---

## 6. Create the legal + content pages

Online Store → **Pages → Add page**. Create these and paste the content from your existing legal
pages (in `public/privacy.html`, `terms.html`, `telehealth-consent.html`, `refund-policy.html` —
copy the body text):

| Page | Handle | Notes |
|---|---|---|
| Privacy Policy | `privacy-policy` | Or use Shopify's Settings → Policies |
| Terms of Service | `terms-of-service` | Or Settings → Policies |
| Refund Policy | `refund-policy` | Or Settings → Policies |
| Telehealth Consent | `telehealth-consent` | Create as a Page |

The footer links auto-resolve to `/policies/...` (if you use Settings → Policies) or `/pages/...`.
Using **Settings → Checkout & Policies** is easiest because Shopify links them into checkout too.

---

## 7. Navigation & the post-checkout HIPAA intake

- **Navigation:** the header/footer links point at homepage sections and your Treatments collection —
  they work out of the box. Set the header CTA target under **Theme settings → Calls to action →
  Primary CTA link** (point it at `/collections/treatments`).
- **The Asher HIPAA medical intake** is the clinical gate. Set it up as an **order-confirmation
  automation**: Settings → Notifications (or a flow app / Shopify Flow) so that right after checkout
  the customer is emailed the **Asher member-portal intake link**. You can also add the link to the
  order-status/"thank you" page. This keeps PHI in Asher's HIPAA system, not in Shopify.

---

## 8. Before you go live (LegitScript + EasyPay)

- [ ] Store is public (remove the password) so LegitScript can scan it.
- [ ] All 5 products live, factual copy, prices shown.
- [ ] Legal pages live and linked.
- [ ] $20 fee + refund rule consistent across product page, cart, checkout, and refund policy.
- [ ] Post-checkout Asher intake automation tested.
- [ ] Test order run through EasyPay end-to-end.
- [ ] Every domain you own (custom domain **and** `*.myshopify.com`) is disclosed to LegitScript and
      compliant.

See `../COMPLIANCE.md` for the full compliance checklist.
