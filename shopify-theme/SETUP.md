# Velacore Health — Shopify theme setup guide

This folder is a complete Shopify theme (the storefront design). The design, homepage,
product page, cart, and legal-page templates are all built. What's left is the **Shopify-admin
configuration** — the parts that can't live in theme code: products, subscription billing, the
EasyPay Direct gateway, pages, and navigation.

Work top to bottom. Nothing here requires a developer.

---

## 0. How the buy flow works right now (MVP)

The product pages are built in a **lead-intake** mode: each product page's **"Start visit"** button
sends the customer to your **JotForm**, so you get a submission notification, then you manually send
the Asher patient link to start the order. No EasyPay/checkout is required to launch this way.

**Set your form URL once:** Online Store → **Customize** → **Theme settings → Intake form → Intake /
JotForm URL** → paste your reworked JotForm link. Every "Start visit" button uses it, and the product
name is appended to the URL (`?product=Tirzepatide…`) so your notification shows which treatment.

> To capture the treatment name inside the JotForm submission, add a **hidden field** in JotForm with
> the unique name `product`. JotForm will auto-fill it from the URL.

When you're ready to sell with real checkout later, sections 3–5 below (subscriptions, EasyPay, the
$20 fee) switch you from JotForm intake to full on-site checkout.

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

**Settled (Asher confirmed in writing, Oct 2026): do NOT charge the $20 in Shopify.** CPOM is ON for
your portal, so the patient pays the $20 Provider Fee directly inside Asher's intake (they add a
payment method there). Your Shopify checkout collects only the **program price**. Don't install a fee
app and don't bake the $20 into the price — either would double-charge the patient.

What Shopify charges vs. what Asher collects:

| Who | What |
|---|---|
| Shopify checkout (you) | Program price (shipping included in the price) |
| Asher intake (patient pays Asher) | $20 Provider Fee, non-refundable |
| Asher invoices you | $10 (single vial) or $30 (multi vial) non-medical fee + $35 shipping + medication cost, only after the physician approves |

Refund rule (matches the legal pages): if the physician declines, refund the **program price** from
Shopify within 15 days. The $20 is non-refundable (Asher keeps it, even on a decline), and no
medication invoice is created for declined orders.

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
- **The Asher HIPAA medical intake** is the clinical gate. Asher's **hosted intake links** (create
  them in the partner portal, one per medication with that medication preselected) are the
  recommended route: they keep PHI in Asher's HIPAA system, not in Shopify or your servers. After
  checkout, send the customer to the matching link via the order-status ("thank you") page and the
  order-confirmation email (Settings → Notifications). Notes from Asher:
  - The links are **reusable across patients** and **can't be pre-filled** with name/email, so the
    patient re-enters their details. Don't publish the links anywhere public (only after payment).
  - **Direct API order creation is not recommended for now:** it would make your backend handle full
    PHI (ID, medical questionnaire, signature). Revisit only with a HIPAA/BAA review.
  - Asher has **no webhooks and no link-generation API**; order status is polling-only.
  - Matching a Shopify order to the Asher order is manual for now (same patient email). Open
    question for Asher: does your final-approval step apply to hosted-link orders, so you can confirm
    the Shopify payment before approving?

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
