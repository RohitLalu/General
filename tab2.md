# Physical Design Implementation Report

## 📊 Design Metrics Summary Table

| Category | Parameter | Value | Unit |
| :--- | :--- | :--- | :--- |
| **Synthesis** | Total Cell Count | 55,508 | count |
| | Number of Wires | 42,830 | count |
| | Number of Wire Bits | 56,111 | bits |
| **Area** | Total Design Area | 598,525 | µm² |
| | Core Utilization | 31.0 | % |
| **Timing** | Worst Negative Slack (WNS) | -544.54 | ns |
| | Total Negative Slack (TNS) | -2,341,430.75 | ns |
| | Clock State | Propagated | - |
| **Power** | Total Power | 1.29e-02 | Watts |
| | Internal Power | 8.37e-03 (65%) | Watts |
| | Switching Power | 4.52e-03 (35%) | Watts |
| | Leakage Power | 2.40e-07 | Watts |
| **Antenna** | Net Violations | 216 | count |
| | Pin Violations | 308 | count |

---

## 🔍 Detailed Data Breakdown

### 1. Cell Statistics (Top 5 by Count)
| Standard Cell Master | Count |
| :--- | :--- |
| `sky130_fd_sc_hd__a21oi_1` | 5,392 |
| `sky130_fd_sc_hd__nor2_1` | 4,904 |
| `sky130_fd_sc_hd__o21ai_0` | 3,784 |
| `sky130_fd_sc_hd__inv_2` | 2,130 |
| `sky130_fd_sc_hd__dfxtp_1` | 1,612 |



### 2. Power Distribution by Group
| Group | Internal (W) | Switching (W) | Total (W) | Percentage |
| :--- | :--- | :--- | :--- | :--- |
| **Sequential** | 5.41e-03 | 1.22e-03 | 6.63e-03 | 51.4% |
| **Clock** | 1.51e-03 | 1.90e-03 | 3.40e-03 | 26.4% |
| **Combinational**| 1.45e-03 | 1.40e-03 | 2.85e-03 | 22.1% |



### 3. Timing Path Analysis
| Path Type | Slack | Startpoint | Endpoint |
| :--- | :--- | :--- | :--- |
| **Setup (Max)** | -544.54 (VIOLATED) | `_86364_` | `_90612_` |
| **Hold (Min)** | 0.06 (MET) | `_96077_` | `_87600_` |



### 4. Antenna Violation Samples
| Net Name | Layer | Max Side Area Ratio | Limit |
| :--- | :--- | :--- | :--- |
| `_00001_[0]` | met1 | 7.69 | 400.00 |
| `_00001_[0]` | met2 | 28.27 | 400.00 |
