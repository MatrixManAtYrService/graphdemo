import json
import networkx as nx
from datetime import datetime, date
from decimal import Decimal
from typing import Dict, Any

from demo.models.ebb.billing_entity import BillingEntity, EntityType
from demo.models.ebb.invoice_info import InvoiceInfo
from demo.models.ebb.fee_rate import FeeRate, ApplyType
from demo.models.ebb.fee_summary import FeeSummary
from demo.models.ebb.settlement import Settlement


def create_node_data(pydantic_obj, table_name: str) -> Dict[str, Any]:
    """Create node data with minimal and others separation."""
    full_dict = pydantic_obj.model_dump()
    minimal_dict = pydantic_obj.to_minimal_dict()
    
    others_dict = {k: v for k, v in full_dict.items() if k not in minimal_dict}
    
    return {
        "table": table_name,
        "minimal": minimal_dict,
        "others": others_dict
    }


def create_pydantic_objects():
    """Create Pydantic objects directly with data."""
    
    # Create billing entities
    merchant_billing_entity = BillingEntity(
        id=1195,
        uuid="JW8H2B9BT6B11R2HHXY3HYQCN6",
        entity_uuid="062X8PVY3XWB1",
        entity_type=EntityType.MERCHANT,
        name="MerchantMcMerchantface",
        created_timestamp=datetime.fromisoformat("2025-02-26T17:06:39.670150"),
        modified_timestamp=datetime.fromisoformat("2025-02-26T17:06:39.670150")
    )
    
    clover_billing_entity = BillingEntity(
        id=1,
        uuid="M4JT4XQCPWPMW7WGA4G1Z5NGED",
        entity_uuid="S7VJZXH057ZHC",
        entity_type=EntityType.RESELLER,
        name="Clover",
        created_timestamp=datetime.fromisoformat("2025-01-30T16:37:56.379038"),
        modified_timestamp=datetime.fromisoformat("2025-01-30T16:37:56.379038")
    )
    
    us_support_billing_entity = BillingEntity(
        id=3,
        uuid="8E7KTPHJRBHP16EQB5RS2P8D0Q",
        entity_uuid="V9Z9C6EX72SY2",
        entity_type=EntityType.RESELLER,
        name="US Customer Support",
        created_timestamp=datetime.fromisoformat("2025-01-30T16:37:56.379038"),
        modified_timestamp=datetime.fromisoformat("2025-01-30T16:37:56.379038")
    )
    
    # Create invoice info
    invoice_info = InvoiceInfo(
        id=6200,
        uuid="NFX80F4EH68BEW08384RX7RBMC",
        billing_entity_uuid="JW8H2B9BT6B11R2HHXY3HYQCN6",
        entity_uuid="062X8PVY3XWB1",
        alternate_id="209225173886",
        billing_date=date.fromisoformat("2025-06-01"),
        invoice_num="202506/000006200",
        currency="USD",
        total_amount=Decimal("258.83"),
        document_uuid="RED0GSNS27W2XG1FQ25VVFEEXH",
        request_uuid="CW6456TXW4N934RVY27G5E5CDB",
        created_timestamp=datetime.fromisoformat("2025-06-02T15:06:43.378289")
    )
    
    # Create fee rates
    fee_rate_1 = FeeRate(
        id=267888,
        uuid="J65DRB7XHQQ1RTYJSBSTQQBW7K",
        billing_entity_uuid="M4JT4XQCPWPMW7WGA4G1Z5NGED",
        fee_category="APP_SUB_3P_RETAIL",
        fee_code="MW63DAWPN6JGY.S",
        currency="USD",
        effective_date=date.fromisoformat("2017-02-15"),
        apply_type=ApplyType.PER_ITEM,
        per_item_amount=Decimal("9.99"),
        percentage=None,
        created_timestamp=datetime.fromisoformat("2025-02-25T19:36:38.626269"),
        modified_timestamp=datetime.fromisoformat("2025-02-25T19:36:38.626269"),
        audit_id=None
    )
    
    fee_rate_2 = FeeRate(
        id=272274,
        uuid="82G1K56V4V17DXXQHGMR3C328W",
        billing_entity_uuid="M4JT4XQCPWPMW7WGA4G1Z5NGED",
        fee_category="APP_SUB_3P_RETAIL",
        fee_code="E2ATEB4GHYFCE.S",
        currency="USD",
        effective_date=date.fromisoformat("2016-02-09"),
        apply_type=ApplyType.PER_ITEM,
        per_item_amount=Decimal("59.99"),
        percentage=None,
        created_timestamp=datetime.fromisoformat("2025-02-25T19:41:08.122154"),
        modified_timestamp=datetime.fromisoformat("2025-02-25T19:41:08.122154"),
        audit_id=None
    )
    
    fee_rate_3 = FeeRate(
        id=244655,
        uuid="VWH1Q0V9SS6FNRD48BYZB9YA9A",
        billing_entity_uuid="M4JT4XQCPWPMW7WGA4G1Z5NGED",
        fee_category="APP_SUB_3P_RETAIL",
        fee_code="BCMPKE5Z10A38.S",
        currency="USD",
        effective_date=date.fromisoformat("2017-02-17"),
        apply_type=ApplyType.PER_ITEM,
        per_item_amount=Decimal("99"),
        percentage=None,
        created_timestamp=datetime.fromisoformat("2025-02-25T19:05:31.108052"),
        modified_timestamp=datetime.fromisoformat("2025-02-25T19:05:31.108052"),
        audit_id=None
    )
    
    fee_rate_4 = FeeRate(
        id=173,
        uuid="2G767D60KKG18208768S4C1HM8",
        billing_entity_uuid="8E7KTPHJRBHP16EQB5RS2P8D0Q",
        fee_category="DEVICE_RETAIL",
        fee_code="RegisterPDVT",
        currency="USD",
        effective_date=date.fromisoformat("2025-01-01"),
        apply_type=ApplyType.PER_ITEM,
        per_item_amount=Decimal("19.95"),
        percentage=None,
        created_timestamp=datetime.fromisoformat("2025-01-30T16:38:02.379723"),
        modified_timestamp=datetime.fromisoformat("2025-01-30T16:38:33.706835"),
        audit_id="STEKRDE0YS244"
    )
    
    fee_rate_5 = FeeRate(
        id=193,
        uuid="KG9ABT30FRKVX39VRV82CBDKJF",
        billing_entity_uuid="8E7KTPHJRBHP16EQB5RS2P8D0Q",
        fee_category="DEVICE_RETAIL_MOD",
        fee_code="RegisterPDVTIncl1st",
        currency="USD",
        effective_date=date.fromisoformat("2025-01-01"),
        apply_type=ApplyType.PER_ITEM,
        per_item_amount=Decimal("-19.95"),
        percentage=None,
        created_timestamp=datetime.fromisoformat("2025-01-30T16:38:02.480183"),
        modified_timestamp=datetime.fromisoformat("2025-01-30T16:38:33.706835"),
        audit_id="STEKRDE0YS244"
    )
    
    fee_rate_6 = FeeRate(
        id=169,
        uuid="DF6FE39FRQHVXJKVVN9WTDSGWX",
        billing_entity_uuid="8E7KTPHJRBHP16EQB5RS2P8D0Q",
        fee_category="PLAN_RETAIL",
        fee_code="RegisterPDVT",
        currency="USD",
        effective_date=date.fromisoformat("2025-01-01"),
        apply_type=ApplyType.PER_ITEM,
        per_item_amount=Decimal("49.95"),
        percentage=None,
        created_timestamp=datetime.fromisoformat("2025-01-30T16:38:02.359401"),
        modified_timestamp=datetime.fromisoformat("2025-01-30T16:38:33.706835"),
        audit_id="STEKRDE0YS244"
    )
    
    # Create fee summaries
    fee_summary_1 = FeeSummary(
        id=74347,
        uuid="K576N1W35XYEVW7VH1JVDY1XRT",
        billing_entity_uuid="JW8H2B9BT6B11R2HHXY3HYQCN6",
        billing_date=date.fromisoformat("2025-06-01"),
        fee_category="APP_SUB_3P_RETAIL",
        fee_code="MW63DAWPN6JGY.S",
        currency="USD",
        total_period_units=Decimal("1"),
        abs_period_units=Decimal("1"),
        total_basis_amount=Decimal("0"),
        abs_basis_amount=Decimal("0"),
        total_fee_amount=Decimal("9.99"),
        fee_rate_uuid="J65DRB7XHQQ1RTYJSBSTQQBW7K",
        request_uuid="KNFZA2P2E2KMGKMATSY1RSD8TY",
        invoice_info_uuid="NFX80F4EH68BEW08384RX7RBMC",
        fee_code_ledger_account_uuid="DMW4K1XGB16DAEQ2ZRSJACE1WS",
        credit_ledger_account_uuid="KBERX62EJMWD8KEVFZRX0H875Z",
        debit_ledger_account_uuid="5XNJ7KBDBGNKVRFZYMCZJ6G5E7",
        exclude_from_invoice=0,
        created_timestamp=datetime.fromisoformat("2025-06-02T14:56:15.960436"),
        modified_timestamp=datetime.fromisoformat("2025-06-02T15:06:43.387646")
    )
    
    fee_summary_2 = FeeSummary(
        id=74345,
        uuid="4FM5SS3WW7WT7GZZWFMSS9YQP6",
        billing_entity_uuid="JW8H2B9BT6B11R2HHXY3HYQCN6",
        billing_date=date.fromisoformat("2025-06-01"),
        fee_category="APP_SUB_3P_RETAIL",
        fee_code="E2ATEB4GHYFCE.S",
        currency="USD",
        total_period_units=Decimal("1"),
        abs_period_units=Decimal("1"),
        total_basis_amount=Decimal("0"),
        abs_basis_amount=Decimal("0"),
        total_fee_amount=Decimal("59.99"),
        fee_rate_uuid="82G1K56V4V17DXXQHGMR3C328W",
        request_uuid="KNFZA2P2E2KMGKMATSY1RSD8TY",
        invoice_info_uuid="NFX80F4EH68BEW08384RX7RBMC",
        fee_code_ledger_account_uuid="2V1BQ7YMC6PJXESE3YA57EW31Q",
        credit_ledger_account_uuid="15WVBBCPN56BD7EGE5STR2R1EW",
        debit_ledger_account_uuid="2MV95DFMWYJ1KZZBGS3HX8F9XN",
        exclude_from_invoice=0,
        created_timestamp=datetime.fromisoformat("2025-06-02T14:56:15.949495"),
        modified_timestamp=datetime.fromisoformat("2025-06-02T15:06:43.387646")
    )
    
    fee_summary_3 = FeeSummary(
        id=74341,
        uuid="MH2Q9759T1FKMP887PMRQFMV9R",
        billing_entity_uuid="JW8H2B9BT6B11R2HHXY3HYQCN6",
        billing_date=date.fromisoformat("2025-06-01"),
        fee_category="APP_SUB_3P_RETAIL",
        fee_code="BCMPKE5Z10A38.S",
        currency="USD",
        total_period_units=Decimal("1"),
        abs_period_units=Decimal("1"),
        total_basis_amount=Decimal("0"),
        abs_basis_amount=Decimal("0"),
        total_fee_amount=Decimal("99"),
        fee_rate_uuid="VWH1Q0V9SS6FNRD48BYZB9YA9A",
        request_uuid="KNFZA2P2E2KMGKMATSY1RSD8TY",
        invoice_info_uuid="NFX80F4EH68BEW08384RX7RBMC",
        fee_code_ledger_account_uuid="AHZXC23GACNTQNYCX9S14PG914",
        credit_ledger_account_uuid="7FQZ30FPEWWM5MV65RY0ZB5D3G",
        debit_ledger_account_uuid="9X9TF60JDBMZQ7A0FHHK7E14W3",
        exclude_from_invoice=0,
        created_timestamp=datetime.fromisoformat("2025-06-02T14:56:15.922833"),
        modified_timestamp=datetime.fromisoformat("2025-06-02T15:06:43.387646")
    )
    
    fee_summary_4 = FeeSummary(
        id=74349,
        uuid="VC74T4AJ9R5X148DSRS95R5PF3",
        billing_entity_uuid="JW8H2B9BT6B11R2HHXY3HYQCN6",
        billing_date=date.fromisoformat("2025-06-01"),
        fee_category="DEVICE_RETAIL",
        fee_code="RegisterPDVT",
        currency="USD",
        total_period_units=Decimal("3"),
        abs_period_units=Decimal("3"),
        total_basis_amount=Decimal("0"),
        abs_basis_amount=Decimal("0"),
        total_fee_amount=Decimal("59.85"),
        fee_rate_uuid="2G767D60KKG18208768S4C1HM8",
        request_uuid="KNFZA2P2E2KMGKMATSY1RSD8TY",
        invoice_info_uuid="NFX80F4EH68BEW08384RX7RBMC",
        fee_code_ledger_account_uuid="JZ4Q82HKC14JDAE8YYZZYWKB0X",
        credit_ledger_account_uuid="HSMJRPH5WVCCV4WKW04CX6ZJG5",
        debit_ledger_account_uuid="62PXBE9JK6QXA65WHY3G5G0K01",
        exclude_from_invoice=0,
        created_timestamp=datetime.fromisoformat("2025-06-02T14:56:15.973521"),
        modified_timestamp=datetime.fromisoformat("2025-06-02T15:06:43.387646")
    )
    
    fee_summary_5 = FeeSummary(
        id=74350,
        uuid="9VEDCKTVN2PTAYAQ8TCQV3ZNGZ",
        billing_entity_uuid="JW8H2B9BT6B11R2HHXY3HYQCN6",
        billing_date=date.fromisoformat("2025-06-01"),
        fee_category="DEVICE_RETAIL_MOD",
        fee_code="RegisterPDVTIncl1st",
        currency="USD",
        total_period_units=Decimal("1"),
        abs_period_units=Decimal("1"),
        total_basis_amount=Decimal("0"),
        abs_basis_amount=Decimal("0"),
        total_fee_amount=Decimal("-19.95"),
        fee_rate_uuid="KG9ABT30FRKVX39VRV82CBDKJF",
        request_uuid="KNFZA2P2E2KMGKMATSY1RSD8TY",
        invoice_info_uuid="NFX80F4EH68BEW08384RX7RBMC",
        fee_code_ledger_account_uuid="H1HH56GWY4VWTDP6VQ3977EKNG",
        credit_ledger_account_uuid="2SNQPEXR2T0PX6Y36NWQSRZNRJ",
        debit_ledger_account_uuid="62PXBE9JK6QXA65WHY3G5G0K01",
        exclude_from_invoice=0,
        created_timestamp=datetime.fromisoformat("2025-06-02T14:56:15.979936"),
        modified_timestamp=datetime.fromisoformat("2025-06-02T15:06:43.387646")
    )
    
    fee_summary_6 = FeeSummary(
        id=74351,
        uuid="FD7GD3YK93ZZS4C1DA6C7W9AER",
        billing_entity_uuid="JW8H2B9BT6B11R2HHXY3HYQCN6",
        billing_date=date.fromisoformat("2025-06-01"),
        fee_category="PLAN_RETAIL",
        fee_code="RegisterPDVT",
        currency="USD",
        total_period_units=Decimal("1"),
        abs_period_units=Decimal("1"),
        total_basis_amount=Decimal("0"),
        abs_basis_amount=Decimal("0"),
        total_fee_amount=Decimal("49.95"),
        fee_rate_uuid="DF6FE39FRQHVXJKVVN9WTDSGWX",
        request_uuid="KNFZA2P2E2KMGKMATSY1RSD8TY",
        invoice_info_uuid="NFX80F4EH68BEW08384RX7RBMC",
        fee_code_ledger_account_uuid="GCCQKS6H40NBQKS6KC4F31WAZY",
        credit_ledger_account_uuid="HSMJRPH5WVCCV4WKW04CX6ZJG5",
        debit_ledger_account_uuid="62PXBE9JK6QXA65WHY3G5G0K01",
        exclude_from_invoice=0,
        created_timestamp=datetime.fromisoformat("2025-06-02T14:56:15.987500"),
        modified_timestamp=datetime.fromisoformat("2025-06-02T15:06:43.387646")
    )
    
    # Create settlements
    settlement_1 = Settlement(
        id=6256,
        uuid="NH8V7V2V0CQ0BWCTGVN6QBV753",
        settlement_date=date.fromisoformat("2025-06-01"),
        billing_entity_uuid="JW8H2B9BT6B11R2HHXY3HYQCN6",
        entity_uuid="062X8PVY3XWB1",
        alternate_id="209225173886",
        payable_receivable="RECEIVABLE",
        currency="USD",
        total_amount=Decimal("9.99"),
        fee_amount=Decimal("9.99"),
        tax1_amount=Decimal("0"),
        tax2_amount=Decimal("0"),
        tax3_amount=Decimal("0"),
        tax4_amount=Decimal("0"),
        lookup_ledger_account_key="Incur.App.E8HJHPCT8AR08",
        gl_code=None,
        item_code="E8HJHPCT8AR08",
        last_invoice_num="202506/000006200",
        request_uuid="CQ95HJ649AXSDG6RF4Z71Z8ATD",
        created_timestamp=datetime.fromisoformat("2025-06-02T16:09:51.666639"),
        modified_timestamp=datetime.fromisoformat("2025-06-02T16:09:52")
    )
    
    settlement_2 = Settlement(
        id=6255,
        uuid="GGG15XMEK13KN6ARGV2F5EXMKT",
        settlement_date=date.fromisoformat("2025-06-01"),
        billing_entity_uuid="JW8H2B9BT6B11R2HHXY3HYQCN6",
        entity_uuid="062X8PVY3XWB1",
        alternate_id="209225173886",
        payable_receivable="RECEIVABLE",
        currency="USD",
        total_amount=Decimal("59.99"),
        fee_amount=Decimal("59.99"),
        tax1_amount=Decimal("0"),
        tax2_amount=Decimal("0"),
        tax3_amount=Decimal("0"),
        tax4_amount=Decimal("0"),
        lookup_ledger_account_key="Incur.App.38NB0ETSWWP6C",
        gl_code=None,
        item_code="38NB0ETSWWP6C",
        last_invoice_num="202506/000006200",
        request_uuid="CQ95HJ649AXSDG6RF4Z71Z8ATD",
        created_timestamp=datetime.fromisoformat("2025-06-02T16:09:51.641654"),
        modified_timestamp=datetime.fromisoformat("2025-06-02T16:09:52")
    )
    
    settlement_3 = Settlement(
        id=6257,
        uuid="8FNKVQ3SSHT2N7AVW3KH8DS00R",
        settlement_date=date.fromisoformat("2025-06-01"),
        billing_entity_uuid="JW8H2B9BT6B11R2HHXY3HYQCN6",
        entity_uuid="062X8PVY3XWB1",
        alternate_id="209225173886",
        payable_receivable="RECEIVABLE",
        currency="USD",
        total_amount=Decimal("99"),
        fee_amount=Decimal("99"),
        tax1_amount=Decimal("0"),
        tax2_amount=Decimal("0"),
        tax3_amount=Decimal("0"),
        tax4_amount=Decimal("0"),
        lookup_ledger_account_key="Incur.App.VX7BFWEXXQ1CW",
        gl_code="51501",
        item_code="VX7BFWEXXQ1CW",
        last_invoice_num="202506/000006200",
        request_uuid="CQ95HJ649AXSDG6RF4Z71Z8ATD",
        created_timestamp=datetime.fromisoformat("2025-06-02T16:09:51.683242"),
        modified_timestamp=datetime.fromisoformat("2025-06-02T16:09:52")
    )
    
    settlement_4 = Settlement(
        id=6258,
        uuid="VS6EVR8GK3AWAKV8SAK4HJFC77",
        settlement_date=date.fromisoformat("2025-06-01"),
        billing_entity_uuid="JW8H2B9BT6B11R2HHXY3HYQCN6",
        entity_uuid="062X8PVY3XWB1",
        alternate_id="209225173886",
        payable_receivable="RECEIVABLE",
        currency="USD",
        total_amount=Decimal("89.85"),
        fee_amount=Decimal("89.85"),
        tax1_amount=Decimal("0"),
        tax2_amount=Decimal("0"),
        tax3_amount=Decimal("0"),
        tax4_amount=Decimal("0"),
        lookup_ledger_account_key="Incur.Plan",
        gl_code="51505",
        item_code="V20071.0000",
        last_invoice_num="202506/000006200",
        request_uuid="CQ95HJ649AXSDG6RF4Z71Z8ATD",
        created_timestamp=datetime.fromisoformat("2025-06-02T16:09:51.700076"),
        modified_timestamp=datetime.fromisoformat("2025-06-02T16:09:52")
    )
    
    return {
        "merchant_billing_entity": merchant_billing_entity,
        "clover_billing_entity": clover_billing_entity,
        "us_support_billing_entity": us_support_billing_entity,
        "invoice_info": invoice_info,
        "fee_rate_1": fee_rate_1,
        "fee_rate_2": fee_rate_2,
        "fee_rate_3": fee_rate_3,
        "fee_rate_4": fee_rate_4,
        "fee_rate_5": fee_rate_5,
        "fee_rate_6": fee_rate_6,
        "fee_summary_1": fee_summary_1,
        "fee_summary_2": fee_summary_2,
        "fee_summary_3": fee_summary_3,
        "fee_summary_4": fee_summary_4,
        "fee_summary_5": fee_summary_5,
        "fee_summary_6": fee_summary_6,
        "settlement_1": settlement_1,
        "settlement_2": settlement_2,
        "settlement_3": settlement_3,
        "settlement_4": settlement_4
    }


def create_graph() -> nx.DiGraph:
    """Create NetworkX graph from the Pydantic objects."""
    G = nx.DiGraph()
    
    # Get all Pydantic objects
    data = create_pydantic_objects()
    
    # Add all nodes
    G.add_node("billing_entity_merchant", **create_node_data(data["merchant_billing_entity"], "billing_entity"))
    G.add_node("billing_entity_clover", **create_node_data(data["clover_billing_entity"], "billing_entity"))
    G.add_node("billing_entity_us_support", **create_node_data(data["us_support_billing_entity"], "billing_entity"))
    G.add_node("invoice_info_1", **create_node_data(data["invoice_info"], "invoice_info"))
    G.add_node("fee_rate_1", **create_node_data(data["fee_rate_1"], "fee_rate"))
    G.add_node("fee_rate_2", **create_node_data(data["fee_rate_2"], "fee_rate"))
    G.add_node("fee_rate_3", **create_node_data(data["fee_rate_3"], "fee_rate"))
    G.add_node("fee_rate_4", **create_node_data(data["fee_rate_4"], "fee_rate"))
    G.add_node("fee_rate_5", **create_node_data(data["fee_rate_5"], "fee_rate"))
    G.add_node("fee_rate_6", **create_node_data(data["fee_rate_6"], "fee_rate"))
    G.add_node("fee_summary_1", **create_node_data(data["fee_summary_1"], "fee_summary"))
    G.add_node("fee_summary_2", **create_node_data(data["fee_summary_2"], "fee_summary"))
    G.add_node("fee_summary_3", **create_node_data(data["fee_summary_3"], "fee_summary"))
    G.add_node("fee_summary_4", **create_node_data(data["fee_summary_4"], "fee_summary"))
    G.add_node("fee_summary_5", **create_node_data(data["fee_summary_5"], "fee_summary"))
    G.add_node("fee_summary_6", **create_node_data(data["fee_summary_6"], "fee_summary"))
    G.add_node("settlement_1", **create_node_data(data["settlement_1"], "settlement"))
    G.add_node("settlement_2", **create_node_data(data["settlement_2"], "settlement"))
    G.add_node("settlement_3", **create_node_data(data["settlement_3"], "settlement"))
    G.add_node("settlement_4", **create_node_data(data["settlement_4"], "settlement"))
    
    # Create explicit connections following the specified flow:
    # billing_entity -> invoice_info -> fee_rate -> fee_summary -> settlement -> other billing_entities
    
    # billing_entity (MerchantMcMerchantface) -> invoice_info
    G.add_edge("billing_entity_merchant", "invoice_info_1")
    
    # invoice_info -> fee_rates (multiple connections)
    G.add_edges_from([
        ("invoice_info_1", "fee_rate_1"),
        ("invoice_info_1", "fee_rate_2"),
        ("invoice_info_1", "fee_rate_3"),
        ("invoice_info_1", "fee_rate_4"),
        ("invoice_info_1", "fee_rate_5"),
        ("invoice_info_1", "fee_rate_6")
    ])
    
    # fee_rates -> fee_summaries (each fee_rate connects to its corresponding fee_summary)
    G.add_edges_from([
        ("fee_rate_1", "fee_summary_1"),  # MW63DAWPN6JGY.S -> 9.99 summary
        ("fee_rate_2", "fee_summary_2"),  # E2ATEB4GHYFCE.S -> 59.99 summary
        ("fee_rate_3", "fee_summary_3"),  # BCMPKE5Z10A38.S -> 99 summary
        ("fee_rate_4", "fee_summary_4"),  # RegisterPDVT (device retail) -> 59.85 summary
        ("fee_rate_5", "fee_summary_5"),  # RegisterPDVTIncl1st (device mod) -> -19.95 summary
        ("fee_rate_6", "fee_summary_6")   # RegisterPDVT (plan retail) -> 49.95 summary
    ])
    
    # fee_summaries -> settlements (based on amounts and flow)
    G.add_edges_from([
        ("fee_summary_1", "settlement_1"),  # 9.99 summary -> 9.99 settlement
        ("fee_summary_2", "settlement_2"),  # 59.99 summary -> 59.99 settlement
        ("fee_summary_3", "settlement_3"),  # 99 summary -> 99 settlement
        ("fee_summary_4", "settlement_4"),  # 59.85 summary -> 89.85 settlement (combined with summary 6)
        ("fee_summary_5", "settlement_4"),  # -19.95 summary -> 89.85 settlement (combined with summary 4)
        ("fee_summary_6", "settlement_4")   # 49.95 summary -> 89.85 settlement (combined with summaries 4,5)
    ])
    
    # settlements -> other billing entities (Clover and US Customer Support)
    G.add_edges_from([
        ("settlement_1", "billing_entity_clover"),
        ("settlement_1", "billing_entity_us_support"),
        ("settlement_2", "billing_entity_clover"),
        ("settlement_2", "billing_entity_us_support"),
        ("settlement_3", "billing_entity_clover"),
        ("settlement_3", "billing_entity_us_support"),
        ("settlement_4", "billing_entity_clover"),
        ("settlement_4", "billing_entity_us_support")
    ])
    
    return G


def serialize_graph(G: nx.DiGraph) -> str:
    """Serialize NetworkX graph to JSON format."""
    graph_data = {
        "nodes": [],
        "edges": []
    }
    
    # Add nodes
    for node_id, node_data in G.nodes(data=True):
        node_entry = {"id": node_id}
        node_entry.update(node_data)
        graph_data["nodes"].append(node_entry)
    
    # Add edges
    for source, target in G.edges():
        graph_data["edges"].append({"source": source, "target": target})
    
    return json.dumps(graph_data, indent=2, default=str)


def main():
    """Main entry point for the graph demo CLI."""
    try:
        graph = create_graph()
        serialized_graph = serialize_graph(graph)
        print(serialized_graph)
    except Exception as e:
        print(f"Error: {e}")
        return 1
    return 0


if __name__ == "__main__":
    main()