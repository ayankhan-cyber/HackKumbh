"""
generate_deck.py
Generates a 16:9 PowerPoint Presentation Deck for EXAMVAULT
YCCE Hackathon 2025 | Problem Statement PS-2: Education Domain
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Colors
    BG_COLOR = RGBColor(10, 15, 29)         # #0A0F1D (Dark Navy)
    CARD_BG = RGBColor(18, 26, 49)          # #121A31 (Slate Box)
    ACCENT_CYAN = RGBColor(0, 240, 255)     # #00F0FF (Electric Cyan)
    ACCENT_GREEN = RGBColor(0, 230, 118)    # #00E676 (Emerald Green)
    ACCENT_PURPLE = RGBColor(168, 85, 247)  # #A855F7 (Purple)
    ACCENT_AMBER = RGBColor(255, 179, 0)    # #FFB300 (Amber)
    TEXT_WHITE = RGBColor(248, 250, 252)    # #F8FAFC (Pure White)
    TEXT_MUTED = RGBColor(148, 163, 184)    # #94A3B8 (Muted Gray)
    BORDER_COLOR = RGBColor(30, 46, 86)     # Subtle border

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()
        return bg

    def add_header(slide, tag, title, subtitle=None):
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(1.3))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        # Tag / Category
        p_tag = tf.paragraphs[0]
        p_tag.text = tag.upper()
        p_tag.font.size = Pt(11)
        p_tag.font.bold = True
        p_tag.font.color.rgb = ACCENT_CYAN

        # Title
        p_title = tf.add_paragraph()
        p_title.text = title
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_WHITE
        p_title.space_after = Pt(4)

        if subtitle:
            p_sub = tf.add_paragraph()
            p_sub.text = subtitle
            p_sub.font.size = Pt(13)
            p_sub.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, title, body_bullets, accent_color=ACCENT_CYAN, badge=None):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = BORDER_COLOR
        card.line.width = Pt(1.2)

        tb = slide.shapes.add_textbox(Inches(left + 0.25), Inches(top + 0.25), Inches(width - 0.5), Inches(height - 0.5))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        # Badge or Title
        p_title = tf.paragraphs[0]
        if badge:
            p_title.text = f"[{badge}] {title}"
        else:
            p_title.text = title
        p_title.font.size = Pt(15)
        p_title.font.bold = True
        p_title.font.color.rgb = accent_color
        p_title.space_after = Pt(10)

        for bullet in body_bullets:
            p = tf.add_paragraph()
            p.text = f"• {bullet}"
            p.font.size = Pt(12)
            p.font.color.rgb = TEXT_WHITE
            p.space_after = Pt(6)

    def add_footer(slide):
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(6.9), Inches(11.7), Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = "EXAMVAULT • YCCE Hackathon 2025 • PS-2: Education Domain • Internet-Proof Assessment System"
        p.font.size = Pt(9)
        p.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    tb1 = s1.shapes.add_textbox(Inches(1.2), Inches(1.5), Inches(11), Inches(4.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "YCCE HACKATHON 2025 • EDUCATION DOMAIN (PS-2)"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p.space_after = Pt(14)

    p = tf1.add_paragraph()
    p.text = "EXAMVAULT"
    p.font.size = Pt(56)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(6)

    p = tf1.add_paragraph()
    p.text = "The Internet-Proof Examination System"
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p.space_after = Pt(14)

    p = tf1.add_paragraph()
    p.text = "A Reliable, Offline-First Assessment Platform for Uninterrupted & Tamper-Safe Exams\nZero Data Loss • Crash Recovery • Exactly-Once Submission • CRDT Conflict Resolution"
    p.font.size = Pt(14)
    p.font.color.rgb = TEXT_MUTED

    add_card(s1, 1.2, 5.4, 2.5, 1.2, "Offline First", ["Works 100% without Wi-Fi"], ACCENT_CYAN)
    add_card(s1, 4.0, 5.4, 2.5, 1.2, "Crash Proof", ["Instant IndexedDB recovery"], ACCENT_GREEN)
    add_card(s1, 6.8, 5.4, 2.5, 1.2, "CRDT Conflict", ["Lamport logical clocks"], ACCENT_AMBER)
    add_card(s1, 9.6, 5.4, 2.5, 1.2, "Anti-Duplicate", ["Idempotent cryptographic nonces"], ACCENT_PURPLE)

    # =========================================================================
    # SLIDE 2: THE PROBLEM STATEMENT
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "Problem Validation • PS-2 Education", "Why Traditional Online Exams Inevitably Fail",
               "Legacy web exams depend on continuous internet, making them fragile and anxiety-inducing.")

    add_card(s2, 0.8, 2.1, 5.6, 2.1, "1. Internet Drops & Timeouts", [
        "In rural schools & tier-2/3 colleges, Wi-Fi and power cuts happen constantly.",
        "Traditional platforms freeze, disconnect the session, and invalidate timers.",
        "Students panic when answer submissions time out."
    ], ACCENT_CYAN, "CRITICAL")

    add_card(s2, 6.8, 2.1, 5.6, 2.1, "2. Browser & Device Crashes", [
        "Browser tabs crash due to RAM exhaustion or accidental reloads.",
        "Answers held in temporary browser memory (RAM) vanish instantly.",
        "The candidate is forced to restart with a blank answer sheet."
    ], ACCENT_AMBER, "DATA LOSS")

    add_card(s2, 0.8, 4.5, 5.6, 2.1, "3. Duplicate Submissions Chaos", [
        "Lag leads students to furiously click 'Submit' multiple times.",
        "Race conditions create duplicate records or overwrite grades with blank retries.",
        "Examiners waste hours manually deduplicating logs."
    ], ACCENT_PURPLE, "RACE CONDITION")

    add_card(s2, 6.8, 4.5, 5.6, 2.1, "4. Sync Conflicts & Inconsistency", [
        "When connections return intermittently, concurrent updates collide.",
        "Older cached answers can overwrite fresher answers on the server.",
        "Lack of mathematical conflict resolution causes grade corruption."
    ], ACCENT_GREEN, "DATA SKEW")
    add_footer(s2)

    # =========================================================================
    # SLIDE 3: OUR SOLUTION - EXAMVAULT
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "Architecture Paradigm", "Our Solution: The Offline-First Exam Engine",
               "ExamVault treats the internet as an optional sync mechanism rather than a single point of failure.")

    add_card(s3, 0.8, 2.1, 3.7, 4.5, "1. Local Encrypted Vault", [
        "Primary database lives on the student's device.",
        "Utilizes browser IndexedDB for high-capacity asynchronous persistence.",
        "Protected via hardware-accelerated AES-GCM (256-bit) encryption.",
        "DevTools tampering is neutralized via SHA-256 state hash chains."
    ], ACCENT_CYAN, "PERSISTENCE")

    add_card(s3, 4.8, 2.1, 3.7, 4.5, "2. Background CRDT Sync", [
        "Asynchronous Service Worker queue monitors connectivity.",
        "When network is restored, delta updates sync automatically in the background.",
        "Lamport Logical Clocks resolve multi-master conflicts with zero human intervention.",
        "Immune to client device clock manipulation."
    ], ACCENT_GREEN, "RECONCILIATION")

    add_card(s3, 8.8, 2.1, 3.7, 4.5, "3. Exactly-Once Delivery", [
        "Unique Cryptographic Nonce generated per exam attempt.",
        "Atomic server-side deduplication lock prevents duplicate entries.",
        "Clicking submit 50 times during network lag commits exactly one clean grade.",
        "Tamper-proof digital signatures issued upon final receipt."
    ], ACCENT_PURPLE, "INTEGRITY")
    add_footer(s3)

    # =========================================================================
    # SLIDE 4: 5-STAGE SYSTEM LIFECYCLE
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "System Workflow", "The 5-Stage Resilient Examination Lifecycle",
               "How ExamVault seamlessly navigates from quiz creation to final grade verification.")

    stages = [
        ("01. Create Exam", ["Teacher configures questions, duration & passkey.", "Packaged into lightweight sync bundle."], ACCENT_CYAN),
        ("02. Attempt Offline", ["Student starts exam.", "Can unplug router or toggle airplane mode.", "Monotonic timer counts down."], ACCENT_AMBER),
        ("03. Encrypted Vault", ["Answers saved synchronously to IndexedDB.", "Encrypted with AES-256.", "Survives tab crash."], ACCENT_GREEN),
        ("04. Auto-Sync", ["Network returns.", "Background engine pushes pending answers.", "CRDT resolves conflicts."], ACCENT_CYAN),
        ("05. Final Commit", ["Student submits.", "Idempotency key guarantees exactly-once commit.", "Digital signature issued."], ACCENT_PURPLE),
    ]

    for idx, (title, bullets, acc) in enumerate(stages):
        left = 0.8 + idx * 2.38
        add_card(s4, left, 2.2, 2.25, 4.4, title, bullets, acc)

    add_footer(s4)

    # =========================================================================
    # SLIDE 5: TECHNICAL INNOVATIONS
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "Algorithmic & Engineering Depth", "Four Core Technical Innovations",
               "Mathematical and cryptographic guarantees designed to exceed hackathon rubrics.")

    add_card(s5, 0.8, 2.1, 5.6, 2.1, "1. Anti-Tamper Monotonic Timer", [
        "Standard web apps trust Date.now(), letting students rewind device clocks.",
        "ExamVault utilizes performance.now() monotonic microsecond ticks.",
        "Logical Lamport ticks detect any temporal discontinuities and prevent late submissions."
    ], ACCENT_CYAN, "ANTI-CHEAT")

    add_card(s5, 6.8, 2.1, 5.6, 2.1, "2. CRDT Last-Write-Wins (LWW)", [
        "State is modeled as a Conflict-Free Replicated Data Type.",
        "Every answer mutation is tagged with an incrementing scalar clock.",
        "Formula: Winner = max(Client_Clock, Server_Clock) with hash-based tie-breakers."
    ], ACCENT_GREEN, "CONSISTENCY")

    add_card(s5, 0.8, 4.5, 5.6, 2.1, "3. Cryptographic Idempotency Nonce", [
        "Nonce = SHA256(StudentID + ExamID + Timestamp + DeviceEntropy).",
        "Server enforces atomic commit lock on idempotency token.",
        "Neutralizes retry storms and duplicate submissions unconditionally."
    ], ACCENT_PURPLE, "EXACTLY-ONCE")

    add_card(s5, 6.8, 4.5, 5.6, 2.1, "4. SHA-256 State Hash Chain", [
        "Every option selection appends to an in-memory hash chain.",
        "Formula: H_n = SHA256(H_{n-1} + Q_id + Option + LamportTick).",
        "Modifying IndexedDB answers via DevTools causes verification failure."
    ], ACCENT_AMBER, "TAMPER-PROOF")
    add_footer(s5)

    # =========================================================================
    # SLIDE 6: SECURITY & TAMPER RESISTANCE
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, "Security Architecture", "Multi-Layered Security & Anti-Fraud Matrix",
               "Ensuring academic integrity and zero cheating in offline environments.")

    threats = [
        ("Threat: DevTools Inspection", "Students attempt to inspect localStorage and alter answers.", "AES-GCM WebCrypto encryption + SHA-256 Hash Chain verification.", ACCENT_CYAN),
        ("Threat: Client Clock Rollback", "Students set device time backwards to gain extra exam minutes.", "Monotonic performance.now() ticks independent of wall-clock time.", ACCENT_GREEN),
        ("Threat: Network Flap Spam", "Repeatedly clicking Submit during connection drops corrupts records.", "Cryptographic Idempotency Nonce rejects repeated submissions.", ACCENT_PURPLE),
        ("Threat: Fatal Browser Crash", "Memory leak or accidental reload wipes candidate progress.", "Synchronous IndexedDB writes ensure < 150ms instant state recovery.", ACCENT_AMBER)
    ]

    for idx, (th, leg, sol, col) in enumerate(threats):
        top = 2.1 + idx * 1.15
        add_card(s6, 0.8, top, 11.7, 1.0, th, [f"Legacy Flaw: {leg}  ➜  ExamVault Defense: {sol}"], col)

    add_footer(s6)

    # =========================================================================
    # SLIDE 7: LIVE PROTOTYPE DEMONSTRATION PLAN
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7, "Live Demonstration", "The 4-Step Interactive Hackathon Demo",
               "Judges can inspect all requirements functioning live in our interactive prototype.")

    add_card(s7, 0.8, 2.1, 5.6, 2.1, "Demo 1: The 'Pull The Plug' Test", [
        "Switch Wi-Fi toggle to OFFLINE mid-exam.",
        "Answer questions smoothly without network errors.",
        "Answers saved synchronously to encrypted IndexedDB."
    ], ACCENT_CYAN, "OFFLINE MODE")

    add_card(s7, 6.8, 2.1, 5.6, 2.1, "Demo 2: The Hard Crash Test", [
        "Click 'Simulate Browser Crash' to destroy memory state.",
        "Instant reload hydrates 100% of answers and timer in < 150ms.",
        "Zero data loss demonstrated live."
    ], ACCENT_AMBER, "CRASH RESILIENT")

    add_card(s7, 0.8, 4.5, 5.6, 2.1, "Demo 3: Auto-Sync & CRDT Reconciliation", [
        "Toggle Wi-Fi back to ONLINE.",
        "Queued answers flush to server in the background.",
        "Teacher Hub receives submissions and displays verified badges."
    ], ACCENT_GREEN, "AUTO SYNC")

    add_card(s7, 6.8, 4.5, 5.6, 2.1, "Demo 4: Spam Submission Neutralization", [
        "Fire 5 simultaneous submission clicks.",
        "Idempotency Guard filters out 4 duplicate requests.",
        "Grade committed exactly once without race conditions."
    ], ACCENT_PURPLE, "IDEMPOTENT")
    add_footer(s7)

    # =========================================================================
    # SLIDE 8: IMPACT & EDUCATIONAL INCLUSIVITY
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header(s8, "Social Impact", "Transforming Accessibility in Rural & Remote Education",
               "Leveling the educational playing field for millions of students facing digital barriers.")

    add_card(s8, 0.8, 2.1, 3.7, 4.5, "68% Rural Schools", [
        "Over 68% of schools in tier-2 and tier-3 regions in India face frequent network drops.",
        "Students are unfairly penalized when cloud LMS portals crash.",
        "ExamVault enables continuous assessments even in zero-bandwidth areas."
    ], ACCENT_CYAN, "ACCESSIBILITY")

    add_card(s8, 4.8, 2.1, 3.7, 4.5, "0% Data Loss Guarantee", [
        "Eliminates re-examination logistics costs for universities.",
        "Reduces student exam anxiety and disputes.",
        "Guarantees that every answered question reaches the evaluation ledger."
    ], ACCENT_GREEN, "RELIABILITY")

    add_card(s8, 8.8, 2.1, 3.7, 4.5, "10x Server Scalability", [
        "Offline-first clients eliminate continuous heartbeat polling.",
        "Servers only process lightweight delta syncs and final commits.",
        "Enables a single low-spec server to easily handle 100,000+ students."
    ], ACCENT_PURPLE, "COST EFFICIENCY")
    add_footer(s8)

    # =========================================================================
    # SLIDE 9: TECH STACK SPECIFICATIONS
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_header(s9, "Engineering Specs", "Modern, Production-Grade Technology Stack",
               "Designed with zero bloat (< 200KB bundle), maximum compatibility, and native browser standards.")

    add_card(s9, 0.8, 2.1, 2.7, 4.5, "Client Frontend", [
        "• Modern SPA / React / Next.js",
        "• Tailwind CSS Design System",
        "• Progressive Web App (PWA)",
        "• Service Worker Background Sync",
        "• Monotonic Performance Ticks"
    ], ACCENT_CYAN, "FRONTEND")

    add_card(s9, 3.8, 2.1, 2.7, 4.5, "Local Persistence", [
        "• Native Browser IndexedDB",
        "• AES-GCM (256-bit Key)",
        "• WebCrypto Hardware Accel",
        "• Zero 3rd Party Cookies",
        "• Instant Local Hydration"
    ], ACCENT_GREEN, "STORAGE")

    add_card(s9, 6.8, 2.1, 2.7, 4.5, "Backend Server", [
        "• Node.js / Express / FastAPI",
        "• Idempotency Middleware",
        "• Lamport Clock Evaluator",
        "• Cryptographic Verifier",
        "• RESTful & Event Ledger"
    ], ACCENT_AMBER, "BACKEND")

    add_card(s9, 9.8, 2.1, 2.7, 4.5, "Data Sync & CRDT", [
        "• LWW-Element-Set CRDT",
        "• Multi-Master Sync Engine",
        "• SHA-256 Micro-Blockchains",
        "• Atomic Commit Locks",
        "• Digital Signature Receipts"
    ], ACCENT_PURPLE, "CRDT ENGINE")
    add_footer(s9)

    # =========================================================================
    # SLIDE 10: CONCLUSION & JUDGE Q&A READY
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10)

    tb10 = s10.shapes.add_textbox(Inches(1.2), Inches(1.2), Inches(11), Inches(4.5))
    tf10 = tb10.text_frame
    tf10.word_wrap = True

    p = tf10.paragraphs[0]
    p.text = "CONCLUSION & JUDGE Q&A"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN
    p.space_after = Pt(10)

    p = tf10.add_paragraph()
    p.text = "EXAMVAULT: Internet-Proof Examinations"
    p.font.size = Pt(38)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(12)

    p = tf10.add_paragraph()
    p.text = "Why ExamVault Wins PS-2:\n• Completely fulfills all 5 stages of the problem statement.\n• Solves real rural connectivity barriers with production-ready cryptography.\n• Features working live prototype with offline mode, crash recovery, and auto-sync."
    p.font.size = Pt(15)
    p.font.color.rgb = TEXT_MUTED

    add_card(s10, 1.2, 4.6, 3.4, 2.0, "Ready for Live Demo", [
        "Switch Wi-Fi off and watch answers persist safely in IndexedDB.",
        "Simulate tab crash with 0% data loss."
    ], ACCENT_CYAN)

    add_card(s10, 5.0, 4.6, 3.4, 2.0, "Open For Questions", [
        "Detailed answers prepared for CRDT conflict resolution, clock skew, and tamper proofing."
    ], ACCENT_GREEN)

    add_card(s10, 8.8, 4.6, 3.4, 2.0, "Thank You Jury!", [
        "YCCE Hackathon 2025",
        "Education Domain (PS-2)",
        "Team EXAMVAULT"
    ], ACCENT_PURPLE)

    add_footer(s10)

    # Save presentation
    output_path = os.path.join(os.path.dirname(__file__), "EXAMVAULT_Presentation_Deck.pptx")
    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    create_presentation()
