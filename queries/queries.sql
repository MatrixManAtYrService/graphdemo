--s
select *
from settlement
where billing_entity_uuid = 'JW8H2B9BT6B11R2HHXY3HYQCN6'
and settlement_date = '2025-06-01';

-- iis
select distinct invoice_info_uuid
from invoice_info_settlement
where settlement_uuid in (
      "GGG15XMEK13KN6ARGV2F5EXMKT"
    , "NH8V7V2V0CQ0BWCTGVN6QBV753"
    , "8FNKVQ3SSHT2N7AVW3KH8DS00R"
    , "VS6EVR8GK3AWAKV8SAK4HJFC77"
    );
-- iin
select * from invoice_info where uuid = 'NFX80F4EH68BEW08384RX7RBMC';
-- la
select * from ledger_account where billing_entity_uuid  = "JW8H2B9BT6B11R2HHXY3HYQCN6";

--fs
select * from fee_summary
where invoice_info_uuid = 'NFX80F4EH68BEW08384RX7RBMC'
and total_fee_amount != 0;

--fr
select fr.*
from fee_rate as fr
 join fee_summary as fs
 on fr.uuid = fs.fee_rate_uuid
where fs.invoice_info_uuid = 'NFX80F4EH68BEW08384RX7RBMC'
 and per_item_amount != 0;

--be
select * from billing_entity
where uuid in (
  "JW8H2B9BT6B11R2HHXY3HYQCN6"
, "M4JT4XQCPWPMW7WGA4G1Z5NGED"
, "8E7KTPHJRBHP16EQB5RS2P8D0Q"
);
