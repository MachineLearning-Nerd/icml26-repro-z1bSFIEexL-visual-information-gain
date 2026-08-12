# Claim 1 VIG definition toy

`src/claim1_vig_definition_toy.py` evaluates the paper’s identity

`VIG = log(PPL_text / PPL_image) = mean(token_loss_text - token_loss_image)`

on four fixed synthetic probability conditions: matching, partial, conflicting, and weak visual support. The outputs demonstrate the expected positive/smaller-positive/negative/near-zero ordering.

This is formula evidence only. It does not run an LVLM, image encoder, blurred-image control, tokenizer, MS-COCO sample, or benchmark.
