# Comparative Analysis: SAST Tools vs AI Models for Vulnerability Detection
## DVPWA Project Assessment

---

## Executive Summary

This analysis evaluates the performance of three Static Application Security Testing (SAST) tools and four AI language models in detecting security vulnerabilities within the Damn Vulnerable Python Web Application (DVPWA) project. Against a groundtruth of 48 documented vulnerabilities, we measured True Positives (TP), False Positives (FP), and False Negatives (FN) to calculate precision, recall, and F1 scores.

**Key Finding**: All evaluated tools demonstrate critically low recall rates (2-29%), indicating that even the best-performing systems miss approximately 70% of known vulnerabilities. This represents a significant security gap that cannot be addressed by traditional SAST tools alone.

---

## Methodology and Metrics

### What We Measured

Our evaluation framework compared tool findings against a curated groundtruth dataset containing 48 known vulnerabilities in the DVPWA codebase. For each tool, we calculated:

- **True Positives (TP)**: Vulnerabilities correctly identified by the tool that exist in the groundtruth
- **False Positives (FP)**: Vulnerabilities reported by the tool that do not exist in the groundtruth
- **False Negatives (FN)**: Groundtruth vulnerabilities the tool failed to detect (calculated as: 48 - TP)

**Note on True Negatives (TN)**: We explicitly excluded TN from our analysis. In vulnerability detection, determining TN would require enumerating all possible non-vulnerable code locations—an infinite or undefined space. Therefore, TN is not a meaningful metric in this context.

### Understanding the Metrics

#### Precision (Accuracy of Findings)
```
Precision = TP / (TP + FP)
```

**What it means**: Of all the vulnerabilities the tool reported, what percentage were actually real vulnerabilities?

**Developer impact**: Low precision leads to **alert fatigue**. When developers receive numerous false alarms, they begin to distrust the tool, potentially ignoring or quickly dismissing legitimate findings. This creates a "boy who cried wolf" scenario that undermines the entire security program.

#### Recall (Coverage of Groundtruth)
```
Recall = TP / (TP + FN) = TP / 48
```

**What it means**: Of all the real vulnerabilities that exist, what percentage did the tool actually find?

**Security impact**: Low recall creates a **false sense of security**. Organizations may believe their code is secure because the tool "passed," while in reality, critical vulnerabilities remain undetected. This is arguably more dangerous than having no tool at all, as it breeds complacency.

#### F1 Score (Balanced Performance)
```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

**What it means**: A harmonic mean that balances precision and recall into a single metric. An F1 score of 1.0 indicates perfect precision and recall; 0.0 indicates complete failure.

**Practical significance**: F1 score helps identify tools that achieve a reasonable balance. A tool with high precision but low recall (or vice versa) may have a low F1 score, indicating it's optimizing for one metric at the expense of the other.

---

## Results Overview

| Tool | TP | FP | FN | Precision | Recall | F1 Score |
|------|----|----|-------|-----------|--------|----------|
| bandit | 2 | 0 | 46 | 100% | 4.17% | 0.08 |
| semgrep | 2 | 0 | 46 | 100% | 4.17% | 0.08 |
| semgrep-pro | 1 | 0 | 47 | 100% | 2.08% | 0.04 |
| gemini-2.5-pro | 4 | 2 | 44 | 66.67% | 8.33% | 0.15 |
| claude-4.5-sonnet | 8 | 3 | 40 | 72.73% | 16.67% | 0.27 |
| gpt-5 | 13 | 1 | 35 | 92.86% | 27.08% | 0.42 |
| grok-4 | 14 | 0 | 34 | 100% | 29.17% | 0.45 |

---

## Analysis: SAST Tools

### The Precision-Recall Trade-off

The three SAST tools evaluated—bandit, semgrep, and semgrep-pro—all achieved **perfect precision (100%)**, meaning every vulnerability they reported was genuine. This is their primary strength and why they remain trusted in CI/CD pipelines: they produce virtually no noise.

However, this comes at a severe cost: **recall rates between 2-4%**. These tools detected only 1-2 vulnerabilities out of 48, missing 96-98% of the security issues present in the codebase.

### Why SAST Tools Have Low Recall

This performance pattern is not a flaw—it's an intentional design choice:

1. **Rule-based detection**: SAST tools rely on predefined patterns and signatures. They can only detect what they've been explicitly programmed to find.

2. **Conservative thresholds**: To maintain high precision, these tools use strict matching criteria, deliberately avoiding any finding that might be a false positive.

3. **Limited context understanding**: SAST tools perform syntactic analysis but struggle with semantic understanding. They cannot reason about data flow, business logic, or context-dependent vulnerabilities.

4. **Scope limitations**: Each tool specializes in certain vulnerability classes. Bandit focuses on Python-specific security issues, semgrep on pattern matching—but neither claims comprehensive coverage.

### The Developer Experience Perspective

From a developer workflow standpoint, SAST tools offer a **low-friction** experience:

- **High trust**: When bandit flags something, developers know it's almost certainly a real issue
- **Minimal interruption**: With only 1-2 findings, the cognitive load is minimal
- **Clear remediation**: Findings usually come with specific, actionable guidance

However, this creates a **critical blind spot**: the other 46 vulnerabilities remain undetected, potentially shipping to production. The absence of alerts is misinterpreted as the absence of problems.

---

## Analysis: AI Language Models

### A Different Trade-off Profile

AI models demonstrate a markedly different performance profile compared to SAST tools:

- **Higher recall**: 8-29% (4-7x better than SAST tools)
- **Variable precision**: 67-100% (most maintain >90% except Gemini)
- **Better F1 scores**: 0.15-0.45 (significantly higher than SAST)

### Why AI Models Perform Differently

1. **Semantic understanding**: Large language models can reason about code context, data flow, and potential attack vectors in ways that pattern-matching cannot.

2. **Generalization**: Rather than relying on hardcoded rules, AI models learn patterns from vast training datasets and can identify novel vulnerability variants.

3. **Holistic analysis**: AI can consider multiple files, understand relationships between components, and reason about how different parts of an application interact.

4. **Configurable sensitivity**: Depending on the prompt and configuration, AI models can adjust their sensitivity threshold, trading precision for recall or vice versa.

### Standout Performer: Grok-4

Grok-4 achieved the best overall performance:
- **14 True Positives** (most detected vulnerabilities)
- **0 False Positives** (perfect precision)
- **34 False Negatives** (still missed 71% of vulnerabilities)
- **F1 Score: 0.45** (highest among all tools)

This represents an exceptional balance: the precision of SAST tools with significantly better coverage. However, even this best-in-class performance still misses the majority of vulnerabilities.

### GPT-5 and Claude: Strong Contenders

GPT-5 came close with 13 TP, 1 FP (92.86% precision), while Claude-4.5-Sonnet found 8 TP with 3 FP (72.73% precision). Both demonstrate that AI models can provide substantial security value while maintaining acceptable false positive rates.

### Gemini: The Precision Challenge

Gemini-2.5-Pro struggled with precision (66.67%), reporting 2 false positives among 6 total findings. In a developer workflow, this 1-in-3 false positive rate would quickly erode trust and contribute to alert fatigue.

---

## Developer Experience and Alert Fatigue

### The Alert Fatigue Problem

Alert fatigue occurs when developers are overwhelmed by security findings, particularly false positives. The psychological impact follows a predictable pattern:

1. **Initial compliance**: Developers investigate all alerts thoroughly
2. **Skepticism**: After encountering false positives, developers become suspicious
3. **Dismissal**: Eventually, developers begin ignoring or batch-closing alerts without investigation
4. **Dangerous complacency**: Real vulnerabilities get dismissed along with false positives

### Precision Thresholds for Developer Trust

Based on research and industry experience, developer tolerance for false positives follows rough thresholds:

- **>95% precision**: High trust, alerts taken seriously
- **90-95% precision**: Acceptable, but requires good UX and clear explanations
- **80-90% precision**: Frustration begins, especially if volume is high
- **<80% precision**: Tool credibility collapses, findings get ignored

In our evaluation:
- **SAST tools (100%)**: Well above trust threshold
- **Grok-4 (100%)**, **GPT-5 (92.86%)**: Within acceptable range
- **Claude (72.73%)**, **Gemini (66.67%)**: Below trust threshold, would cause alert fatigue

### Volume Considerations

Alert fatigue is a function of both precision AND volume:

- **Low volume + low precision**: 3 FP out of 11 findings (Claude) is annoying but manageable
- **High volume + low precision**: 300 FP out of 1,100 findings would be catastrophic

In the DVPWA context:
- **SAST tools**: 1-2 findings—minimal cognitive load
- **AI models**: 6-14 findings—still manageable, but precision becomes critical

For larger codebases, if these ratios hold, AI models might generate dozens or hundreds of findings. At that scale, precision below 90% becomes a serious operational problem.

---

## The False Sense of Security Problem

### The Danger of Low Recall

While alert fatigue from false positives is disruptive, **low recall is existentially dangerous** for security programs:

1. **Undetected vulnerabilities ship to production**: 34-47 critical vulnerabilities in DVPWA were missed by all tools
2. **Compliance theater**: Organizations check the "we ran security tools" box without achieving actual security
3. **Misallocated resources**: Teams invest in fixing the 2-14 detected issues while 34-46 others remain
4. **False confidence**: Stakeholders believe the application is secure because "the tools found no issues"

### Real-World Implications

In a production environment, the vulnerabilities these tools miss could include:

- SQL injections leading to data breaches
- Authentication bypasses enabling unauthorized access
- XSS vulnerabilities compromising user sessions
- Authorization flaws exposing sensitive operations

The fact that even the best tool (Grok-4) detected only 29% of vulnerabilities means **71% of security risks remain invisible** to automated detection.

### The Regulatory and Compliance Dimension

Many compliance frameworks (PCI-DSS, HIPAA, SOC2) require organizations to "implement security testing tools." Our findings reveal a critical gap:

- **Compliance requirement**: "Use SAST tools" ✓
- **Actual security outcome**: 96% of vulnerabilities undetected ✗

This highlights the difference between **compliance** (checking boxes) and **security** (actually protecting systems).

---

## Strategic Implications

### The Fundamental Limitation of Automated Tools

Our findings underscore a crucial reality: **no single automated tool provides comprehensive vulnerability coverage**. Even combining all seven tools tested would still leave gaps:

- Different tools find overlapping issues (multiple tools found the same 1-2 vulnerabilities)
- Many vulnerability classes require human reasoning, business context, or manual testing
- Complex logic flaws, race conditions, and architectural issues often evade automated detection

### The Case Against Tool Consolidation

Organizations often seek a "single pane of glass" security solution. Our data suggests this approach is fundamentally flawed:

- **SAST tools** excel at precision but miss most vulnerabilities
- **AI models** improve recall but introduce precision challenges
- **Combining both** is necessary but still insufficient for comprehensive coverage

A robust security program requires:
1. Multiple complementary automated tools (SAST + AI + dependency scanning + secrets detection)
2. Manual security reviews and penetration testing
3. Secure development training for engineers
4. Architecture and design reviews

### The ROI Question

From a resource allocation perspective:

**SAST tools** offer the best ROI for CI/CD integration:
- Zero false positives = zero wasted developer time
- Fast execution
- Clear, actionable findings
- But: catch only 2-4% of vulnerabilities

**AI models** offer potential for deeper analysis:
- Find 4-7x more vulnerabilities
- Can reason about complex scenarios
- But: require more careful tuning, validation, and developer education
- Risk of alert fatigue if not properly configured

**Optimal strategy**: Use SAST tools as a baseline quality gate (block deployments on TP findings), then layer AI-assisted reviews for deeper coverage, accepting some false positives in exchange for better recall.

---

## Recommendations

### For Security Teams

1. **Set realistic expectations**: Automated tools are a starting point, not a complete solution
2. **Measure and report recall**: Don't just track "findings remediated"—track "coverage of known vulnerability classes"
3. **Layered defense**: Combine SAST, AI analysis, manual reviews, and penetration testing
4. **Invest in training**: Help developers understand both the tools' capabilities and their limitations

### For Development Teams

1. **Don't ignore AI findings reflexively**: Even with some false positives, 90%+ precision means most findings are real
2. **Provide feedback**: Help security teams tune AI models by reporting false positives
3. **Understand the gaps**: Just because a tool passed doesn't mean the code is secure
4. **Participate in security reviews**: Automated tools can't replace human expertise

### For Tool Selection

1. **SAST tools**: Essential for CI/CD gates; prioritize based on language/framework coverage
2. **AI models**: Valuable for code review augmentation; choose based on precision and integration quality
3. **Hybrid approach**: Use SAST for automated blocking, AI for advisory findings
4. **Continuous evaluation**: Regularly reassess tool effectiveness against your actual vulnerability landscape

### For Future Research

Our analysis reveals several areas requiring further investigation:

1. **Tool combination strategies**: How can we optimally combine multiple tools to maximize recall while managing precision?
2. **Prompt engineering for AI models**: Can we improve AI precision without sacrificing recall through better prompting?
3. **Developer feedback loops**: How does providing clear false positive feedback improve AI model accuracy over time?
4. **Context-specific tuning**: Do these performance metrics hold across different application types, languages, and domains?

---

## Limitations of This Study

### Groundtruth Constraints

Our evaluation assumes the groundtruth dataset (48 vulnerabilities) is comprehensive and accurate. In reality:
- Additional vulnerabilities may exist that weren't documented
- Some documented issues may be false positives in the groundtruth itself
- Severity classifications may be subjective

### Single Application Context

DVPWA is a deliberately vulnerable application designed for training. Performance may differ on:
- Production codebases with better security practices
- Different languages and frameworks
- Larger, more complex applications
- Legacy code vs. modern code

### Snapshot in Time

SAST tools and AI models evolve rapidly:
- Tool versions and rule sets were current at evaluation time
- AI models receive regular updates and improvements
- Future versions may perform significantly better (or worse)

### Configuration Variables

AI model performance heavily depends on:
- Prompt engineering and instructions
- Temperature and sampling parameters
- Context window size and chunking strategies
- Single-shot vs. multi-turn analysis

Different configurations could yield substantially different results.

---

## Conclusions

### The Core Dilemma

Our analysis reveals an uncomfortable truth: organizations face a choice between **high precision with minimal coverage** (SAST tools) and **better coverage with precision challenges** (AI models). Neither option provides adequate security on its own.

The data demonstrates that:

1. **SAST tools are trustworthy but insufficient**: Perfect precision means developers can rely on their findings, but 2-4% recall means they're missing the vast majority of security issues.

2. **AI models show promise but need refinement**: 4-7x better recall represents significant progress, but precision variability creates operational challenges that could undermine adoption.

3. **No tool is a silver bullet**: Even the best performer (Grok-4) detected less than one-third of known vulnerabilities, leaving substantial security gaps.

### The Path Forward

The future of automated vulnerability detection likely involves:

- **Hybrid approaches** that combine the strengths of SAST (precision) and AI (semantic understanding)
- **Contextual tuning** where tools adapt to specific codebases, reducing false positives over time
- **Human-in-the-loop workflows** that leverage AI to augment rather than replace security expertise
- **Continuous learning systems** that improve from developer feedback on false positives

### Final Thoughts

The metrics tell a clear story: we are still in the early stages of automated vulnerability detection. While tools have improved dramatically, the gap between "what tools can find" and "what vulnerabilities actually exist" remains enormous.

For organizations serious about security, the answer isn't choosing between SAST and AI—it's thoughtfully integrating both, while recognizing that automated tools are one component of a comprehensive security program that must include manual review, architectural analysis, threat modeling, and ongoing security training.

The developer experience matters: tools that generate excessive false positives will be ignored, no matter how good their recall. But security outcomes matter more: tools that miss 70-98% of vulnerabilities create dangerous blind spots, no matter how precise they are.

Balancing these competing concerns—developer productivity and security effectiveness—remains the central challenge of application security tooling.

---

**Analysis Date**: 2025-10-10
**Dataset**: DVPWA (48 groundtruth vulnerabilities)
**Tools Evaluated**: bandit, semgrep, semgrep-pro, gemini-2.5-pro, claude-4.5-sonnet, gpt-5, grok-4
