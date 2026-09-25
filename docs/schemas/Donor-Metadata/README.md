# Donor Metadata Schema

Document Status: _Endorsed BICAN Standard_

Version: 1.0

Owner: @memartone

Reviewers: @patrick-lloyd-ray, @carolth, @rightbower

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: 23-09-2023

## Overview

The BICAN Donor Metadata schema specifies the metadata relating to donors in BICAN. These metadata reflect the metadata needed to accurately track donors and related entities from the brain banks through the specimen portal. As such, it is a collaborative schema that reflects the joint efforts of members of BICAN. 

Note that there are additional fields in the metadata schema which are not explicitly required at time of creation, but will be populated when relevant resources are created/updated. 

This document has the following sections:

* [General Requirements](#general-requirements)
* [General Subject Fields](#general-subject-fields)
* [General Specimen Data](#general-specimen-metadata)
* [Non-Brain Specimen Collected](#non-brain-specimen-collected)
* [Diagnoses](#diagnoses)
* [Infant Medical History](#infant-medical-history)
* [Perinatal Neurologic Events](#perinatal-neurologic-events)
* [Family History](#family-history)
* [Infectious Disease Testing](#infectious-disease-testing)
* [Toxicology Screening](#toxicology-screening)
* [Neuropathological Diagnoses](#neuropathological-diagnoses)
* [Appendix](#appendix)
* [Changelog](#changelog)

## General Requirements

[brief description of general requirements]

## General Subject Fields

### Local Donor ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Local Donor ID</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf</td>
    </tr>    
</tbody></table>
<br>

### Repository

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Repository</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>inclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>408682ed-0e27-41e2-b9fa-f05674366d6e</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Donor Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>donor source</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>inclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0d0cf732-0f76-409d-9a73-7a96d829d3d3</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Ethnicity

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>ethnicity</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>918370df-49f6-4361-9c52-f46b16412980</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Race

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>race</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e515c009-550e-4f9c-b1b6-fc876a6fb2a8</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Secondary Race

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>secondary_race</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>192fe5b1-c812-4767-86fb-3178f9914705</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Sex at Birth

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>sex at birth</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c819b9d5-2fde-40b2-bf0d-e07b56f96ac9</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Gender at Time of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>gender at time of death</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>1c71e775-65aa-442b-a392-1cf9a44e326e</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Sexual Orientation at Time of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>sexual orientation at time of death</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e47e8a2f-72fb-4036-b288-f4580dc2aa4e</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Age Value (Years)

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>age at death</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>14eb923a-161d-45e2-889d-81fea7b632b6</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Birth Country Name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>birth country name</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>9c27fd29-b512-492f-a32f-b615c7585ff7</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Primary Language Code

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>primary language code</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A human-readable, locally unique label that identifies a data collection.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>abe9edc7-96ca-4c6a-a1ed-c008548cc373</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Secondary Language Code

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>secondary language code</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>37b7495f-b010-4d1c-ae32-9cb19c680950</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Date of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>date of death</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>date</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>60445046-d9d8-4f00-959e-9a4c42613e5e</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Autopsy Report

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>autopsy report</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3f787b64-0985-4d0f-9523-54475164b7ad</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Cause of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cause of death</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>inclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>fa970a03-41ea-473b-a8ce-427fec92cdff</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Cause of Death Code

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cause of death code</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>inclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>61374624-2d3c-477e-95b3-9bd30974b52a</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Manner of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>manner of death</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>36eeb35b-5020-4a9e-a74b-6e1104415e0e</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Marital or Partner Status ATOD

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>marital or partner status at time of death</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4f0e41c9-dd15-4a37-ae6b-11b7131d7cba</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Education Years Number

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>education years number</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>add3f7fe-ae60-4cc1-bb2e-72bbbe9a1a7d</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Family Income Range

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>family income range</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6cd785e2-7333-43fe-8c8c-c19532e96ea6</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Informant Questionnaire Completed

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>informant questionnaire completed</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e8b9666f-a112-456f-aa5a-69a101c3866f</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Informant Interview Performed

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>informant interview performed</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>274b838b-74c6-46ec-808a-0c080ddeedd9</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Informant Relationship

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>informant relationship</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>836c19fe-b735-4bf7-bee5-3213122b571e</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Informant Relationship Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>informant relationship specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>289bcbb8-5177-4c65-b0af-159fd65b69aa</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Handedness

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>handedness</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>82a4087c-d0e3-48ca-8bea-a81eefc683a0</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Medical Records Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>medical records available</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ee2c9223-f7d1-4c64-a1da-cd7408309955</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Medical Records Reviewed

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>medical records reviewed</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6139b159-c36c-4501-9176-fe2741e3d448</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### HBCAC Confirmation Status

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>confirmed_hbcac</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b6cdddf7-6f0b-4855-a0fa-16c2ab29f219</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Consent Status

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>consent_status</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>1a53e733-276f-421a-850d-eb46e50db972</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## General Specimen Data

### Hemisphere

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>hemisphere</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>68b7a28b-d695-4ec9-800b-6a27ca206081</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Post-Mortem Interval

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>post mortem interval</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6fd5c5ac-b128-4a4a-ae98-09eaeba22f92</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Left Hemisphere Preparation

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>left hemisphere preparation</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>57d5378f-a451-4bf5-a472-cc88d0d29586</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Left Hemisphere Preparation Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>left hemisphere preparation specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>002e915e-01c3-4570-a1f3-76680dcb2c33</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Right Hemisphere Preparation

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>right hemisphere preparation</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>477c2600-f979-43c5-9c61-ab61fd771584</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Right Hemisphere Preparation Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>right hemisphere preparation specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>efd50be4-f7cf-4146-a08e-28f25680728c</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### RIN

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>rin</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>cd472c0d-0b64-45c9-a38e-e54d15cea953</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### RIN Tissue Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>rin tissue source</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d547ee51-9ec3-489c-8e49-7d8cd94080a8</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### RIN Testing Organization

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>rin testing organization</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>cfed831e-9a62-4a32-bf92-532873420eb3</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### RINe

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>rine</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>1210148d-d8fb-45aa-b51a-4b19b6d09bec</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### RINe Tissue Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>rine tissue source</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>7d5fd9af-82a1-4bdb-a3c6-9225d1717c53</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### RINe Testing Organization

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>rine testing organization</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>15a6d162-a3ca-4852-b626-a911c37c04c9</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### pH

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>pH</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>9e67af02-c081-43e1-a42c-bf9603cae616</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Brain Weight

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain weight</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>546fc32d-f8a2-4c00-924a-8c4730f11f51</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Brain Tissue Weighed Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain tissue weighed type</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a7463e3f-0c61-4718-a7d0-60fd2116908a</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Photo 2D Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>photo 2D available</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>611beda8-1ac6-4183-a284-04a30bb474f3</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Scan 3D Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>scan 3D available</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>658e8a80-e232-438f-8c1e-d5f38724dc55</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Antemortem MRI Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>antemortem MRI available</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>43a04caa-4f28-47ac-8a9d-74c40f10776f</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Postmortem MRI Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>postmortem MRI available</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0badd072-0c25-48c6-9357-44d5b5bc0818</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Postmortum MRI Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>postmortem MRI type</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>64a607a9-21e6-4c73-8f2e-2d67b0dc51c8</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Antatomical Atlas Registration

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>anatomical atlas registration</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b6835813-2bab-42f3-ae63-4c372ed0aad9</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>


## Non-Brain Specimen Collected

### Non-Brain Tissue Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>non-brain tissue available</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3a064c96-a956-4cf3-8b77-056b8e392f99</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Tissue Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>tissue type</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>33ccbc85-ae35-44d6-8bc6-c2fb91116cf7</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Tissue Type Details

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>tissue type details</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f551cf87-2c6e-4b92-888d-6310e6a500d8</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Subject ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>subject ID</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b2bb8225-aa6e-423a-a32d-98feaf84984f</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Tissue Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>tissue source</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ee83ecf8-4fca-4353-a9ed-4cdd82eb167e</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Date of Collection

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>date of collection</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>date</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>9b94949c-a7c9-4d81-a1c9-a70c96c16ca3</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Age at Date of Collection

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>age at date of collection</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6c53ac16-fe2d-48d7-b3d4-b8946b5d2547</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Diagnoses

### Clinical Brain Diagnosis Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>clinical brain diagnosis available</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b49f026b-4f6c-48c8-b170-bf6d24c672ef</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Clinical Brain Diagnosis Code

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>clinical brain diagnosis code</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b7a34c73-ae08-43d3-80d2-d5ef8436e449</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Clinical Brain Diagnosis Confidence Level

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>clinical brain diagnosis confidence level</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>2e72b4b9-d5fb-4f0d-897c-1f977ed4fabd</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Genetic Diagnosis Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>genetic diagnosis available</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f67d3837-159d-4868-9749-aa6c83ded7eb</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Genetic Diagnosis Code

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>genetic diagnosis code</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>7a7916e0-ff79-4426-b49f-58e2f2a8a367</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Genetic Diagnosis Confidence Level

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>genetic diagnosis confidence level</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>cb2b0108-8c07-40e8-92a3-b693b6dc64b4</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Non-Brain Diagnosis Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>non-brain diagnosis available</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>009ec58e-32e4-4712-930c-056e72c8d8fa</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Non-Brain Diagnosis Code

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>non-brain diagnosis code</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>65e8824e-01d2-44cf-9f47-9962461a65c9</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Non-Brain Diagnosis Confidence Level

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>non-brain diagnosis confidence level</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>2a7ff937-287b-40a3-a1f6-ebf598683774</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Infant Medical History

### Birth Weight lbs

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>birth weight lbs</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>69d9a60d-32d5-4c3a-a26a-802d8f030c8d</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Birth Weight ozs

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>birth weight ozs</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b6f30050-f762-4427-8533-31738e737ea2</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Gestational Age Value Weeks

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>gestational age value weeks</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6d8a9b3f-792c-48c2-bd3c-56e52bb51672</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Gestational Age Value Days

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>gestational age value days</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4e532e52-6e4c-46cd-9fde-96f97ef3b034</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### APGAR 5 Minute Score Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>APGAR 5 minute score available</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e67d93ac-3753-4835-a250-e2ca207b2675</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### APGAR 5 Minute Score

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>APGAR 5 minute score</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3a10dabf-39b0-4eb7-8399-85fd325c5646</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### APGAR 10 Minute Score Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>APGAR 10 minute score available</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3d085ff9-7034-487d-a2b2-b9ae80d55333</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### APGAR 10 Minute Score

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>APGAR 10 minute score</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>09d512b6-7c20-4693-8894-77824ad7f04d</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Perinatal Neurologic Events

### Perinatal Neurologic Event Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>perinatal neurologic event type</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>cb4c7e3b-73fc-400e-a4c3-b149a5544363</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Perinatal Neurologic Event Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>perinatal neurologic event type specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>1bf1f9c5-79a6-4203-910f-cad79fe9cac9</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Family History

### Family History Availalble

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>family history available</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c88bf4dc-5a7c-4f70-a773-e6bbb5a12ec9</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Relative Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>relative type</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>1adef34c-bb96-4dd0-bc87-51868f2ddc3f</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Relative Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>relative type specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>094064a1-362c-4b75-8556-6b874c843fdb</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Condition Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>condition type</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>030c8275-04c0-4e4f-9f68-48fd0f559250</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Condition Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>condition type specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a1ed23dc-3cd5-41c8-87f6-58604fc66a70</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Infectious Disease Testing

### Test Name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>test name</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b6865e15-7538-4890-be99-a6f9e9920af3</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Test Result

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>test result</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c14ea006-662c-4666-bfd1-6ff580c403ed</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Tissue Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>testing tissue source</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>42f8e11b-d9a3-48fe-ac1e-cd6f4469de46</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Toxicology Screening

### Drugs Found

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>drugs found</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e35b53f1-0daa-4b5b-9246-cfba52f61bfb</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Drugs Found Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>drugs found specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ec3f7c47-9062-4b66-ba80-a9355a388bc0</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Toxicology Result

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>toxicology result</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>2cf1a1af-1ece-4ef7-b513-e4d1949f237c</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Toxicology Report Level

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>toxicology report level</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>594179b0-c744-40a4-958d-fc81461b4b74</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Toxicology Units

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>toxicology units</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6f124149-50de-489d-b9e2-f198b2b9857d</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Neuropathological Diagnoses

### Artifacts

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>artifacts</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b344b605-21dd-4e06-9104-21005179026f</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Artifacts Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>artifacts type</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>dc217b9b-ed6b-48e2-93b4-4f648dc395f7</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Artifacts Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>artifacts type specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ae11485d-dfc6-45fe-9d22-1d0bf7244d7c</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Neuropathology Diagnosis Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>neuropathology_diagnosis</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>87f6d251-e028-4480-9272-3497655fb9cd</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Neuropathology Diagnosis Code

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>neuropathology_diagnosis_code</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>784e9cc1-7258-4535-a6d5-f7f9a4c2da4b</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Developmental

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>developmental</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c259cdc2-7c68-48de-ab57-57328f3bddfa</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Developmental Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>developmental type specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>bee7d477-2dec-4bf5-878e-a105a0054366</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Inflammatory

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>inflammatory</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>05e83583-078d-4a1e-892d-e6f611e5a0b8</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Inflammatory Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>inflammatory type specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>616ba8d8-ced3-4f3e-b1ca-7103eb7a2c94</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Infectious

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>infectious</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>266f5fb8-716b-4472-be30-4a94b62f2245</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Infectious Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>infectious type specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c73cea5e-44d1-4dd9-b55e-3c6ef5dd2ef2</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Traumatic

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>traumatic</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a00497c0-376f-4b2e-b60e-d6add2af41dc</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Traumatic Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>traumatic type</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>01d2f488-f30b-40e0-913f-c9adc6b39b97</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Traumatic Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>traumatic type specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>aa574a9a-a3d0-4a07-bf8b-9db4a1110a88</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Vascular

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>vascular</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b02d8386-d059-42a8-94cb-751d56b15b3a</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Vascular Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>vascular type</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>5beafa90-ffdb-4cce-a78c-a3b3175210b6</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Vascular Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>vascular type specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>543acbbb-9da4-4e24-a9d7-c0642aa33f32</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Neoplastic

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>neoplastic</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3f52a0e9-6469-46d3-8ed5-3cdb8afdc259</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Neoplastic Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>neoplastic type</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a58be8f4-2756-4a66-9d05-1fbf44b4e810</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Neoplastic Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>neoplastic type specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b9e8aead-fdf3-453e-a46b-fcb01d661f8f</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Aging

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>aging</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>40e3caa7-657b-4137-9879-07e6b29bae14</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Aging Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>aging type</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>5e31b66f-131e-4d5e-8760-ddd85f5634d5</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Aging Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>aging type specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>8667d972-175c-430a-ac5e-656563e75736</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Neurodegenerative

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>neurodegenerative</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>764d80ce-7a83-4e68-92df-34a416475e1b</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Neurodegenerative Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>neurodegenerative type</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b150b62c-a968-4f5d-9aa3-d1ab5207ff83</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Neurodegenerative Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>neurodegenerative type specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d422d827-539f-4d10-b09d-0f4be00d7c91</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Appendix

<!-- schema-properties-start -->
## Schema properties
*Auto-generated from CSV. Do not edit this section manually.*

**Status:** Endorsed BICAN Standard &middot; **Version:** 1.0.0 &middot; **Date:** 2023-04-01

### Properties

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`subject_id`](#subject_id) | — | no | Local Donor ID | An identifier that uniquely denotes objects only within the scope of a specific object aggregate and that is not registe… |
| [`repository`](#repository) | — | no | Repository | Repository&#x27; trailing modifier (qualifier, &#x27;repository&#x27;) of &#x27;xref&#x27; links of &#x27;Format&#x27; concepts. When &#x27;true&#x27;, the link is p… |
| [`donor_source`](#donor_source) | — | no | Donor Source | The origin of the donor/subject in this experiment. |
| [`ethnicity`](#ethnicity) | — | no | Ethnicity | Population category defined in terms of cultural, religious, tribal or other social similarities. [EFO] |
| [`race`](#race) | — | no | Race | An arbitrary classification of a taxonomic group that is a division of a species. It usually arises as a consequence of … |
| [`secondary_race`](#secondary_race) | — | no | Secondary Race | The non-primary race category of a donor. |
| [`sex`](#sex) | — | no | Sex at Birth | An organismal quality inhering in a bearer by virtue of the bearer&#x27;s ability to undergo sexual reproduction in order to … |
| [`gender`](#gender) | — | no | Gender at Time of Death | Identification as male/masculine, female/feminine or something else, and association with a (social) role or set of beha… |
| [`sex_orientation`](#sex_orientation) | — | no | Sexual Orientation at Time of Death | The pattern of a person&#x27;s emotional, romantic, and/or sexual attractions. [NCIT] |
| [`age_at_death`](#age_at_death) | — | no | Age Value (Years) | A time quality inhering in a bearer by virtue of how long the bearer has existed. [PATO] |
| [`birth_country_name`](#birth_country_name) | — | no | Birth Country Name | The name of the country where a subject was born. [NCIT] |
| [`primary_language`](#primary_language) | — | no | Primary Language Code | The alphanumeric code from the ISO 639 standard which denotes the primary lanugage of a subject. The ISO 639 standard in… |
| [`secondary_language`](#secondary_language) | — | no | Secondary Language Code | The alphanumeric code from the ISO 639 standard which denotes the secondary lanugage of a subject. The ISO 639 standard … |
| [`year_of_death`](#year_of_death) | — | no | Date of Death | The year wherein the subject or donor has ceased to exist. |
| [`autopsy_report`](#autopsy_report) | — | no | Autopsy Report | A document assembled by an author for the purpose of providing information regarding the cause of death of a subject for… |
| [`cause_of_death`](#cause_of_death) | — | no | Cause of Death | The circumstance or condition that results in the death of a living being. [NCIT] |
| [`cause_of_death_code`](#cause_of_death_code) | — | no | Cause of Death Code | The ISO code that denotes the circumstance or condition that results in the death of a living being. [NCIT] |
| [`manner_of_death`](#manner_of_death) | — | no | Manner of Death | The manner of death is the determination of how the injury or disease leads to death.  There are five manners of death (… |
| [`marital_status`](#marital_status) | — | no | Marital or Partner Status ATOD | The marital or partner status of the donor at time of death. |
| [`education_years_number`](#education_years_number) | — | no | Education Years Number | The level of education of a donor given in number of years. |
| [`family_income_range`](#family_income_range) | — | no | Family Income Range | The income of the donor&#x27;s family given as a range. |
| [`informant_questionnaire_completed`](#informant_questionnaire_completed) | — | no | Informant Questionnaire Completed | The status (completed, not completed) of the document about the subject completed by an informant. |
| [`informant_interview_performed`](#informant_interview_performed) | — | no | Informant Interview Performed | The status (performed, not performed) of the interview event between a clinician and an informant. |
| [`informant_relationship`](#informant_relationship) | — | no | Informant Relationship | The relationship that an informant bears to a subject/donor. |
| [`informant_relationship_specify`](#informant_relationship_specify) | — | no | Informant Relationship Specify | The specific relationship that an informant bears to a subject/donor. |
| [`handedness`](#handedness) | — | no | Handedness | A behavioral quality inhering ina bearer by virtue of the bearer&#x27;s unequal distribution of fine motor skill between its … |
| [`medical_records_available`](#medical_records_available) | — | no | Medical Records Available | The status (available, unavailable) of the medical records of the subject/donor. |
| [`medical_records_reviewed`](#medical_records_reviewed) | — | no | Medical Records Reviewed | The status (reviewed, not reviewed) of the medical records of the subject/donor. |
| [`confirmed_hbcac`](#confirmed_hbcac) | — | no | HBCAC Confirmation Status | The donor&#x27;s Huntington Breast Cancer Action Coalition status. |
| [`consent_status`](#consent_status) | — | no | Consent Status | The donor&#x27;s consent status. |
| [`hemisphere`](#hemisphere) | — | no | Hemisphere | One of two bilateral, largely symmetrical organ subdivisions within the telencephalon which contain the cerebral cortex … |
| [`post_mortem_interval`](#post_mortem_interval) | — | no | Post Mortem Interval | The length of the temporal interval between the time of death of the subject/donor and the time at which the specimen is… |
| [`left_hemisphere_preparation`](#left_hemisphere_preparation) | — | no | Left Hemisphere Preparation | The type of preparation method used for the left hemisphere. |
| [`left_hemisphere_preparation_specify`](#left_hemisphere_preparation_specify) | — | no | Left Hemisphere Preparation Specify | Specific details about the type of preparation method used for the left hemisphere. |
| [`right_hemisphere_preparation`](#right_hemisphere_preparation) | — | no | Right Hemisphere Preparation | The type of preparation method used for the right hemisphere. |
| [`right_hemisphere_preparation_specify`](#right_hemisphere_preparation_specify) | — | no | Right Hemisphere Preparation Specify | Specific details about the type of preparation method used for the right hemisphere. |
| [`rin`](#rin) | — | no | RIN | The RNA integrity number value of a specimen. |
| [`rin_tissue_source`](#rin_tissue_source) | — | no | RIN Tissue Source | The tissue sample location or identifier that is used for calculating the RNA integrity number. |
| [`rin_testing_organization`](#rin_testing_organization) | — | no | RIN Testing Organization | The organization that determines the RNA integrity number of a sample/specimen. |
| [`rine`](#rine) | — | no | RINe | A type of RIN (RNA integrity number) value that represents the relative ratio of the signal in the fast zone to the 18S … |
| [`rine_tissue_source`](#rine_tissue_source) | — | no | RINe Tissue Source | The tissue sample location or identifier that is used for calculating the RINe number. |
| [`rine_testing_organization`](#rine_testing_organization) | — | no | RINe Testing Organization | The organization that determines the RINe number. |
| [`ph`](#ph) | — | no | pH | The value of a measurement of acidity or basicity of a tissue, sample, or specimen. |
| [`brain_weight`](#brain_weight) | — | no | Brain Weight Measurement | The weight of a brain specimen. |
| [`weighed_type`](#weighed_type) | — | no | Brain Tissue Weighed Type | The state of a brain specimen when it is weighed (fresh, frozen, fixed). |
| [`photo_2d_available`](#photo_2d_available) | — | no | Photo 2d Available | The status (available, unavailable) of two-dimensional photos of a subject/donor/specimen. |
| [`scan_3d_available`](#scan_3d_available) | — | no | Scan 3d Available | The status (available, unavailable) of three-dimensional scans of a subject/donor/specimen. |
| [`antemortem_mri_available`](#antemortem_mri_available) | — | no | Antemortem MRI Available | The status (available, unavailable) of antemortem MRI images of a subject/donor/specimen. |
| [`postmortem_mri_available`](#postmortem_mri_available) | — | no | Postmortem MRI Available | The status (available, unavailable) of postmortem MRI images of a subject/donor/specimen. |
| [`postmortem_mri_type`](#postmortem_mri_type) | — | no | Postmortem MRI Type | The type of postmortem MRI that is available (cadeveric, fresh ex vivo, fixed ex vivo). |
| [`anatomical_atlas_registration`](#anatomical_atlas_registration) | — | no | Anatomical Atlas Registration | The anatomical atlas structure to which a specimen/tissue is registered. |
| [`non_brain_tissue_available`](#non_brain_tissue_available) | — | no | Non-Brain Tissue Available | The status (yes, no) of whether non-brain tissue from this organism is available. |
| [`tissue_type`](#tissue_type) | — | no | Tissue Type | The type of tissue (non-brain) that is available from this organism. |
| [`tissue_type_details`](#tissue_type_details) | — | no | Tissue Type Details | The details of the non-brain tissue that is available from this organism. |
| [`tissue_source`](#tissue_source) | — | no | Tissue Source | The source of the non-brain tissue that is available from this organism. |
| [`date_of_collection`](#date_of_collection) | — | no | Date of Collection | The date that the tissue collection occurred. |
| [`age_at_date_of_collection`](#age_at_date_of_collection) | — | no | Age at Date of Collection | The age of the donor at the date of tissue collection (years). |
| [`clinical_brain_diagnosis`](#clinical_brain_diagnosis) | — | no | Clinical Brain Diagnosis Available | The status (available/unavailable) of the clinical brain diagnosis of the donor. |
| [`clinical_brain_diagnosis_code`](#clinical_brain_diagnosis_code) | — | no | Clinical Brain Diagnosis Code | The code of the donor&#x27;s clinical brain diagnosis. |
| [`clinical_brain_diagnosis_confidence_level`](#clinical_brain_diagnosis_confidence_level) | — | no | Clinical Brain Diagnosis Confidence Level | The confidence level of the donor&#x27;s clinical brain diagnosis. |
| [`genetic_diagnosis`](#genetic_diagnosis) | — | no | Genetic Diagnosis Available | The status (available, unavailable) of the genetic diagnosis of the donor. |
| [`genetic_diagnosis_code`](#genetic_diagnosis_code) | — | no | Genetic Diagnosis Code | The code of the donor&#x27;s genetic diagnosis. |
| [`genetic_diagnosis_confidence_level`](#genetic_diagnosis_confidence_level) | — | no | Genetic Diagnosis Confidence Level | The confidence level of the donor&#x27;s genetic diagnosis. |
| [`non_brain_diagnosis`](#non_brain_diagnosis) | — | no | Non Brain Diagnosis Available | The status (available, unavailable) of a non-brain diagnosis of the donor. |
| [`non_brain_diagnosis_code`](#non_brain_diagnosis_code) | — | no | Non Brain Diagnosis Code | The code of the donor&#x27;s non-brain diagnosis. |
| [`non_brain_diagnosis_confidence_level`](#non_brain_diagnosis_confidence_level) | — | no | Non Brain Diagnosis Confidence Level | The confidence level of the donor&#x27;s non-brain diagnosis. |
| [`birth_weight_lbs`](#birth_weight_lbs) | — | no | Birth Weight Value (lbs) | The weight (at birth) of the subject/donor in pounds. |
| [`birth_weight_oz`](#birth_weight_oz) | — | no | Birth Weight Value (oz) | The weight (at birth) of the subject/donor in ounces. |
| [`gestational_age_value_weeks`](#gestational_age_value_weeks) | — | no | Gestational Age Value (weeks) | The gestational age of the subject/donor in weeks. |
| [`gestational_age_value_days`](#gestational_age_value_days) | — | no | Gestational Age Value (days) | The gestational age of the subject/donor in days. |
| [`apgar_5_minute_score_available`](#apgar_5_minute_score_available) | — | no | APGAR Five Minute Score Available | The status (available, unavailable) of a five-minute APGAR score of the donor. |
| [`apgar_5_minute_score`](#apgar_5_minute_score) | — | no | APGAR Five Minute Score | The score of the donor&#x27;s five-minute APGAR. |
| [`apgar_10_minute_score_available`](#apgar_10_minute_score_available) | — | no | APGAR Ten Minute Score Available | The status (available, unavailable) of a ten-minute APGAR score of the donor. |
| [`apgar_10_minute_score`](#apgar_10_minute_score) | — | no | APGAR Ten Minute Score | The score of the donor&#x27;s ten-minute APGAR. |
| [`perinatal_neurologic_event_type`](#perinatal_neurologic_event_type) | — | no | Perinatal Neurologic Event Type | The perinatal neurologic event of a donor. |
| [`perinatal_neurologic_event_type_specify`](#perinatal_neurologic_event_type_specify) | — | no | Perinatal Neurologic Event Type Specify | The specific perinatal neurologic event of a donor. |
| [`family_history_available`](#family_history_available) | — | no | Family History Available | The status (available, unavailable) of the family history of the subject/donor. |
| [`relative_type`](#relative_type) | — | no | Relative Type | The familial relation to the subject/donor. |
| [`relative_type_specify`](#relative_type_specify) | — | no | Relative Type Specify | The specific familial relation to the subject/donor. |
| [`condition_type`](#condition_type) | — | no | Condition Type | A condition of the donor. |
| [`condition_type_specify`](#condition_type_specify) | — | no | Condition Type Specify | A specific type of condition of a donor. |
| [`test_name`](#test_name) | — | no | Test Name | The name of the test that has been performed. |
| [`test_result`](#test_result) | — | no | Result | The result(s) of the test that has been performed. |
| [`tissue_source`](#tissue_source) | — | no | Testing Tissue Source | The tissue sample location or identifier that is the subject of a test. |
| [`drugs_found`](#drugs_found) | — | no | Drugs Found | A list of drugs found present in a donor. |
| [`drugs_found_specify`](#drugs_found_specify) | — | no | Drugs Found Specify | A list of specific drugs found present in a donor. |
| [`toxicology_result`](#toxicology_result) | — | no | Toxicology Result | The toxicology result of the donor. |
| [`toxicology_report_level`](#toxicology_report_level) | — | no | Toxicology Report level | The report level of the toxicology result of the donor. |
| [`toxicology_units`](#toxicology_units) | — | no | Toxicology Units | The units of the report level of the toxicology result of the donor. |
| [`artifacts`](#artifacts) | — | no | Artifacts | The neuropathology artifacts available for a donor. |
| [`artifacts_type`](#artifacts_type) | — | no | Artifacts Type | The type of neuropathology artifacts available for a donor. |
| [`artifacts_type_specify`](#artifacts_type_specify) | — | no | Artifacts Type Specify | The specific types of neuropathology artifacts available for a donor. |
| [`neuropathology_diagnosis`](#neuropathology_diagnosis) | — | no | Neuropathology Diagnosis Available | The neuropathology diagnosis of a donor. |
| [`neuropathology_diagnosis_code`](#neuropathology_diagnosis_code) | — | no | Neuorpathology Diagnosis Code | The code of the donor&#x27;s neuropathology diagnosis. |
| [`developmental`](#developmental) | — | no | Developmental | The type of developmental disorder or disease of a donor. |
| [`developmental_type_specify`](#developmental_type_specify) | — | no | Developmental Type Specify | The specific type of developmental disorder or disease of a donor. |
| [`inflammatory`](#inflammatory) | — | no | Inflammatory | The type of inflammatory disorder or disease of a donor. |
| [`inflammatory_type_specify`](#inflammatory_type_specify) | — | no | Inflammatory Type Specify | The specific type of inflammatory disorder or disease of a donor. |
| [`infectious`](#infectious) | — | no | Infectious | The type of infectious disease of a donor. |
| [`infectious_type_specify`](#infectious_type_specify) | — | no | Infectious Type Specify | The specific type of infectious disease of a donor. |
| [`traumatic`](#traumatic) | — | no | Traumatic | The trauma of a donor. |
| [`traumatic_type`](#traumatic_type) | — | no | Traumatic Type | The type of trauma of a donor. |
| [`traumatic_type_specify`](#traumatic_type_specify) | — | no | Traumatic Type Specify | The specific type of trauma of a donor. |
| [`vascular`](#vascular) | — | no | Vascular | The vascular disease of a donor. |
| [`vascular_type`](#vascular_type) | — | no | Vascular Type | The type of vascular disease of a donor. |
| [`vascular_type_specify`](#vascular_type_specify) | — | no | Vascular Type Specify | The specific type of vascular disease of a donor. |
| [`neoplastic`](#neoplastic) | — | no | Neoplastic | The neoplastic status of a donor. |
| [`neoplastic_type`](#neoplastic_type) | — | no | Neoplastic Type | The type of neoplastic status of a donor. |
| [`neoplastic_type_specify`](#neoplastic_type_specify) | — | no | Neoplastic Type Specify | The specific type of neoplastic status of a donor. |
| [`aging`](#aging) | — | no | Aging | A developmental process that is a deterioration and loss of function over time. Aging includes loss of functions such as… |
| [`aging_type`](#aging_type) | — | no | Aging Type | The type of aging of a donor. |
| [`aging_type_specify`](#aging_type_specify) | — | no | Aging Type Specify | The specific type of aging of a donor. |
| [`neurodegenerative`](#neurodegenerative) | — | no | Neurodegenerative | A disorder of the central nervous system characterized by gradual and progressive loss of neural tissue and neurologic f… |
| [`neurodegenerative_type`](#neurodegenerative_type) | — | no | Neurodegenerative Type | The type of neurodegenerative disorder of a donor. |
| [`neurodegenerative_type_specify`](#neurodegenerative_type_specify) | — | no | Neurodegenerative Type Specify | The specific type of neurodegenerative disorder of a donor. |

### Property Details

<div id="subject_id" class="field-detail">
<h5><code>subject_id</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf</code></li>
<li><strong>Aliases:</strong> Local Donor ID</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>An identifier that uniquely denotes objects only within the scope of a specific object aggregate and that is not registered in an identifier registry. [Allotrope]</p>
</div>

<div id="repository" class="field-detail">
<h5><code>repository</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>408682ed-0e27-41e2-b9fa-f05674366d6e</code></li>
<li><strong>Aliases:</strong> Repository</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>Repository&#x27; trailing modifier (qualifier, &#x27;repository&#x27;) of &#x27;xref&#x27; links of &#x27;Format&#x27; concepts. When &#x27;true&#x27;, the link is pointing to the public source-code repository where the given data format is developed or maintained. [EDAM]</p>
</div>

<div id="donor_source" class="field-detail">
<h5><code>donor_source</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>0d0cf732-0f76-409d-9a73-7a96d829d3d3</code></li>
<li><strong>Aliases:</strong> Donor Source</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>The origin of the donor/subject in this experiment.</p>
</div>

<div id="ethnicity" class="field-detail">
<h5><code>ethnicity</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>918370df-49f6-4361-9c52-f46b16412980</code></li>
<li><strong>Aliases:</strong> Ethnicity</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>Population category defined in terms of cultural, religious, tribal or other social similarities. [EFO]</p>
</div>

<div id="race" class="field-detail">
<h5><code>race</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>e515c009-550e-4f9c-b1b6-fc876a6fb2a8</code></li>
<li><strong>Aliases:</strong> Race</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>An arbitrary classification of a taxonomic group that is a division of a species. It usually arises as a consequence of geographical isolation within a species and is characterized by shared heredity, physical attributes and behavior, and in the case of humans, by common history, nationality, or geographic distribution. [ExO]</p>
</div>

<div id="secondary_race" class="field-detail">
<h5><code>secondary_race</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>192fe5b1-c812-4767-86fb-3178f9914705</code></li>
<li><strong>Aliases:</strong> Secondary Race</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>The non-primary race category of a donor.</p>
</div>

<div id="sex" class="field-detail">
<h5><code>sex</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>c819b9d5-2fde-40b2-bf0d-e07b56f96ac9</code></li>
<li><strong>Aliases:</strong> Sex at Birth</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>An organismal quality inhering in a bearer by virtue of the bearer&#x27;s ability to undergo sexual reproduction in order to differentiate the individuals or types involved. [PATO]</p>
</div>

<div id="gender" class="field-detail">
<h5><code>gender</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>1c71e775-65aa-442b-a392-1cf9a44e326e</code></li>
<li><strong>Aliases:</strong> Gender at Time of Death</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>Identification as male/masculine, female/feminine or something else, and association with a (social) role or set of behavioral and cultural traits, clothing, etc; a category to which a person belongs on this basis. Gender is the result of a complex combination of gender role, gender expression, gender identity, and gender modality. Do not use this term for non-human animals. [NCIT]</p>
</div>

<div id="sex_orientation" class="field-detail">
<h5><code>sex_orientation</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>e47e8a2f-72fb-4036-b288-f4580dc2aa4e</code></li>
<li><strong>Aliases:</strong> Sexual Orientation at Time of Death</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>The pattern of a person&#x27;s emotional, romantic, and/or sexual attractions. [NCIT]</p>
</div>

<div id="age_at_death" class="field-detail">
<h5><code>age_at_death</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>14eb923a-161d-45e2-889d-81fea7b632b6</code></li>
<li><strong>Aliases:</strong> Age Value (Years)</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
<li><strong>Range:</strong> 0 – 125 year</li>
</ul>
<p>A time quality inhering in a bearer by virtue of how long the bearer has existed. [PATO]</p>
</div>

<div id="birth_country_name" class="field-detail">
<h5><code>birth_country_name</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>9c27fd29-b512-492f-a32f-b615c7585ff7</code></li>
<li><strong>Aliases:</strong> Birth Country Name</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>The name of the country where a subject was born. [NCIT]</p>
</div>

<div id="primary_language" class="field-detail">
<h5><code>primary_language</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>abe9edc7-96ca-4c6a-a1ed-c008548cc373</code></li>
<li><strong>Aliases:</strong> Primary Language Code</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>The alphanumeric code from the ISO 639 standard which denotes the primary lanugage of a subject. The ISO 639 standard includes a two letter representation and a three letter representation. [NCIT, modified]</p>
</div>

<div id="secondary_language" class="field-detail">
<h5><code>secondary_language</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>37b7495f-b010-4d1c-ae32-9cb19c680950</code></li>
<li><strong>Aliases:</strong> Secondary Language Code</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>The alphanumeric code from the ISO 639 standard which denotes the secondary lanugage of a subject. The ISO 639 standard includes a two letter representation and a three letter representation. [NCIT, modified]</p>
</div>

<div id="year_of_death" class="field-detail">
<h5><code>year_of_death</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>60445046-d9d8-4f00-959e-9a4c42613e5e</code></li>
<li><strong>Aliases:</strong> Date of Death</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
<li><strong>Range:</strong> 1900 – 2050 CE</li>
</ul>
<p>The year wherein the subject or donor has ceased to exist.</p>
</div>

<div id="autopsy_report" class="field-detail">
<h5><code>autopsy_report</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>3f787b64-0985-4d0f-9523-54475164b7ad</code></li>
<li><strong>Aliases:</strong> Autopsy Report</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>A document assembled by an author for the purpose of providing information regarding the cause of death of a subject for the audience. [IAO, modified]</p>
</div>

<div id="cause_of_death" class="field-detail">
<h5><code>cause_of_death</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>fa970a03-41ea-473b-a8ce-427fec92cdff</code></li>
<li><strong>Aliases:</strong> Cause of Death</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>The circumstance or condition that results in the death of a living being. [NCIT]</p>
</div>

<div id="cause_of_death_code" class="field-detail">
<h5><code>cause_of_death_code</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>61374624-2d3c-477e-95b3-9bd30974b52a</code></li>
<li><strong>Aliases:</strong> Cause of Death Code</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>The ISO code that denotes the circumstance or condition that results in the death of a living being. [NCIT]</p>
</div>

<div id="manner_of_death" class="field-detail">
<h5><code>manner_of_death</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>36eeb35b-5020-4a9e-a74b-6e1104415e0e</code></li>
<li><strong>Aliases:</strong> Manner of Death</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>The manner of death is the determination of how the injury or disease leads to death.  There are five manners of death (natural, accident, suicide, homicide, and undetermined).</p>
</div>

<div id="marital_status" class="field-detail">
<h5><code>marital_status</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>4f0e41c9-dd15-4a37-ae6b-11b7131d7cba</code></li>
<li><strong>Aliases:</strong> Marital or Partner Status ATOD</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>The marital or partner status of the donor at time of death.</p>
</div>

<div id="education_years_number" class="field-detail">
<h5><code>education_years_number</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>add3f7fe-ae60-4cc1-bb2e-72bbbe9a1a7d</code></li>
<li><strong>Aliases:</strong> Education Years Number</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
<li><strong>Range:</strong> 0 – 30 year</li>
</ul>
<p>The level of education of a donor given in number of years.</p>
</div>

<div id="family_income_range" class="field-detail">
<h5><code>family_income_range</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>6cd785e2-7333-43fe-8c8c-c19532e96ea6</code></li>
<li><strong>Aliases:</strong> Family Income Range</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>The income of the donor&#x27;s family given as a range.</p>
</div>

<div id="informant_questionnaire_completed" class="field-detail">
<h5><code>informant_questionnaire_completed</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>e8b9666f-a112-456f-aa5a-69a101c3866f</code></li>
<li><strong>Aliases:</strong> Informant Questionnaire Completed</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>The status (completed, not completed) of the document about the subject completed by an informant.</p>
</div>

<div id="informant_interview_performed" class="field-detail">
<h5><code>informant_interview_performed</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>274b838b-74c6-46ec-808a-0c080ddeedd9</code></li>
<li><strong>Aliases:</strong> Informant Interview Performed</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>The status (performed, not performed) of the interview event between a clinician and an informant.</p>
</div>

<div id="informant_relationship" class="field-detail">
<h5><code>informant_relationship</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>836c19fe-b735-4bf7-bee5-3213122b571e</code></li>
<li><strong>Aliases:</strong> Informant Relationship</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>The relationship that an informant bears to a subject/donor.</p>
</div>

<div id="informant_relationship_specify" class="field-detail">
<h5><code>informant_relationship_specify</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>289bcbb8-5177-4c65-b0af-159fd65b69aa</code></li>
<li><strong>Aliases:</strong> Informant Relationship Specify</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>The specific relationship that an informant bears to a subject/donor.</p>
</div>

<div id="handedness" class="field-detail">
<h5><code>handedness</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>82a4087c-d0e3-48ca-8bea-a81eefc683a0</code></li>
<li><strong>Aliases:</strong> Handedness</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>A behavioral quality inhering ina bearer by virtue of the bearer&#x27;s unequal distribution of fine motor skill between its left and right hands or feet. [PATO]</p>
</div>

<div id="medical_records_available" class="field-detail">
<h5><code>medical_records_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>ee2c9223-f7d1-4c64-a1da-cd7408309955</code></li>
<li><strong>Aliases:</strong> Medical Records Available</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>The status (available, unavailable) of the medical records of the subject/donor.</p>
</div>

<div id="medical_records_reviewed" class="field-detail">
<h5><code>medical_records_reviewed</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>6139b159-c36c-4501-9176-fe2741e3d448</code></li>
<li><strong>Aliases:</strong> Medical Records Reviewed</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>The status (reviewed, not reviewed) of the medical records of the subject/donor.</p>
</div>

<div id="confirmed_hbcac" class="field-detail">
<h5><code>confirmed_hbcac</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b6cdddf7-6f0b-4855-a0fa-16c2ab29f219</code></li>
<li><strong>Aliases:</strong> HBCAC Confirmation Status</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>The donor&#x27;s Huntington Breast Cancer Action Coalition status.</p>
</div>

<div id="consent_status" class="field-detail">
<h5><code>consent_status</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>1a53e733-276f-421a-850d-eb46e50db972</code></li>
<li><strong>Aliases:</strong> Consent Status</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>The donor&#x27;s consent status.</p>
</div>

<div id="hemisphere" class="field-detail">
<h5><code>hemisphere</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>68b7a28b-d695-4ec9-800b-6a27ca206081</code></li>
<li><strong>Aliases:</strong> Hemisphere</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>One of two bilateral, largely symmetrical organ subdivisions within the telencephalon which contain the cerebral cortex and cerebral white matter. [UBERON]</p>
</div>

<div id="post_mortem_interval" class="field-detail">
<h5><code>post_mortem_interval</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>6fd5c5ac-b128-4a4a-ae98-09eaeba22f92</code></li>
<li><strong>Aliases:</strong> Post Mortem Interval</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
<li><strong>Range:</strong> 0 – 8888 hour</li>
</ul>
<p>The length of the temporal interval between the time of death of the subject/donor and the time at which the specimen is made.</p>
</div>

<div id="left_hemisphere_preparation" class="field-detail">
<h5><code>left_hemisphere_preparation</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>57d5378f-a451-4bf5-a472-cc88d0d29586</code></li>
<li><strong>Aliases:</strong> Left Hemisphere Preparation</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>The type of preparation method used for the left hemisphere.</p>
</div>

<div id="left_hemisphere_preparation_specify" class="field-detail">
<h5><code>left_hemisphere_preparation_specify</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>002e915e-01c3-4570-a1f3-76680dcb2c33</code></li>
<li><strong>Aliases:</strong> Left Hemisphere Preparation Specify</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>Specific details about the type of preparation method used for the left hemisphere.</p>
</div>

<div id="right_hemisphere_preparation" class="field-detail">
<h5><code>right_hemisphere_preparation</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>477c2600-f979-43c5-9c61-ab61fd771584</code></li>
<li><strong>Aliases:</strong> Right Hemisphere Preparation</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>The type of preparation method used for the right hemisphere.</p>
</div>

<div id="right_hemisphere_preparation_specify" class="field-detail">
<h5><code>right_hemisphere_preparation_specify</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>efd50be4-f7cf-4146-a08e-28f25680728c</code></li>
<li><strong>Aliases:</strong> Right Hemisphere Preparation Specify</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>Specific details about the type of preparation method used for the right hemisphere.</p>
</div>

<div id="rin" class="field-detail">
<h5><code>rin</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>cd472c0d-0b64-45c9-a38e-e54d15cea953</code></li>
<li><strong>Aliases:</strong> RIN</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
<li><strong>Range:</strong> 0 – 99</li>
</ul>
<p>The RNA integrity number value of a specimen.</p>
</div>

<div id="rin_tissue_source" class="field-detail">
<h5><code>rin_tissue_source</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>d547ee51-9ec3-489c-8e49-7d8cd94080a8</code></li>
<li><strong>Aliases:</strong> RIN Tissue Source</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>The tissue sample location or identifier that is used for calculating the RNA integrity number.</p>
</div>

<div id="rin_testing_organization" class="field-detail">
<h5><code>rin_testing_organization</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>cfed831e-9a62-4a32-bf92-532873420eb3</code></li>
<li><strong>Aliases:</strong> RIN Testing Organization</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>The organization that determines the RNA integrity number of a sample/specimen.</p>
</div>

<div id="rine" class="field-detail">
<h5><code>rine</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>1210148d-d8fb-45aa-b51a-4b19b6d09bec</code></li>
<li><strong>Aliases:</strong> RINe</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
<li><strong>Range:</strong> 0 – 99</li>
</ul>
<p>A type of RIN (RNA integrity number) value that represents the relative ratio of the signal in the fast zone to the 18S peak signal fpr a specimen.</p>
</div>

<div id="rine_tissue_source" class="field-detail">
<h5><code>rine_tissue_source</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>7d5fd9af-82a1-4bdb-a3c6-9225d1717c53</code></li>
<li><strong>Aliases:</strong> RINe Tissue Source</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>The tissue sample location or identifier that is used for calculating the RINe number.</p>
</div>

<div id="rine_testing_organization" class="field-detail">
<h5><code>rine_testing_organization</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>15a6d162-a3ca-4852-b626-a911c37c04c9</code></li>
<li><strong>Aliases:</strong> RINe Testing Organization</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>The organization that determines the RINe number.</p>
</div>

<div id="ph" class="field-detail">
<h5><code>ph</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>9e67af02-c081-43e1-a42c-bf9603cae616</code></li>
<li><strong>Aliases:</strong> pH</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
<li><strong>Range:</strong> 0 – 99</li>
</ul>
<p>The value of a measurement of acidity or basicity of a tissue, sample, or specimen.</p>
</div>

<div id="brain_weight" class="field-detail">
<h5><code>brain_weight</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>546fc32d-f8a2-4c00-924a-8c4730f11f51</code></li>
<li><strong>Aliases:</strong> Brain Weight Measurement</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
<li><strong>Range:</strong> 0 – 9998 gram</li>
</ul>
<p>The weight of a brain specimen.</p>
</div>

<div id="weighed_type" class="field-detail">
<h5><code>weighed_type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>a7463e3f-0c61-4718-a7d0-60fd2116908a</code></li>
<li><strong>Aliases:</strong> Brain Tissue Weighed Type</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>The state of a brain specimen when it is weighed (fresh, frozen, fixed).</p>
</div>

<div id="photo_2d_available" class="field-detail">
<h5><code>photo_2d_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>611beda8-1ac6-4183-a284-04a30bb474f3</code></li>
<li><strong>Aliases:</strong> Photo 2d Available</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>The status (available, unavailable) of two-dimensional photos of a subject/donor/specimen.</p>
</div>

<div id="scan_3d_available" class="field-detail">
<h5><code>scan_3d_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>658e8a80-e232-438f-8c1e-d5f38724dc55</code></li>
<li><strong>Aliases:</strong> Scan 3d Available</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>The status (available, unavailable) of three-dimensional scans of a subject/donor/specimen.</p>
</div>

<div id="antemortem_mri_available" class="field-detail">
<h5><code>antemortem_mri_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>43a04caa-4f28-47ac-8a9d-74c40f10776f</code></li>
<li><strong>Aliases:</strong> Antemortem MRI Available</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>The status (available, unavailable) of antemortem MRI images of a subject/donor/specimen.</p>
</div>

<div id="postmortem_mri_available" class="field-detail">
<h5><code>postmortem_mri_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>0badd072-0c25-48c6-9357-44d5b5bc0818</code></li>
<li><strong>Aliases:</strong> Postmortem MRI Available</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>The status (available, unavailable) of postmortem MRI images of a subject/donor/specimen.</p>
</div>

<div id="postmortem_mri_type" class="field-detail">
<h5><code>postmortem_mri_type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>64a607a9-21e6-4c73-8f2e-2d67b0dc51c8</code></li>
<li><strong>Aliases:</strong> Postmortem MRI Type</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>The type of postmortem MRI that is available (cadeveric, fresh ex vivo, fixed ex vivo).</p>
</div>

<div id="anatomical_atlas_registration" class="field-detail">
<h5><code>anatomical_atlas_registration</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b6835813-2bab-42f3-ae63-4c372ed0aad9</code></li>
<li><strong>Aliases:</strong> Anatomical Atlas Registration</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>The anatomical atlas structure to which a specimen/tissue is registered.</p>
</div>

<div id="non_brain_tissue_available" class="field-detail">
<h5><code>non_brain_tissue_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>3a064c96-a956-4cf3-8b77-056b8e392f99</code></li>
<li><strong>Aliases:</strong> Non-Brain Tissue Available</li>
<li><strong>Subsets:</strong> Non-Brain Specimen Collected</li>
</ul>
<p>The status (yes, no) of whether non-brain tissue from this organism is available.</p>
</div>

<div id="tissue_type" class="field-detail">
<h5><code>tissue_type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>33ccbc85-ae35-44d6-8bc6-c2fb91116cf7</code></li>
<li><strong>Aliases:</strong> Tissue Type</li>
<li><strong>Subsets:</strong> Non-Brain Specimen Collected</li>
</ul>
<p>The type of tissue (non-brain) that is available from this organism.</p>
</div>

<div id="tissue_type_details" class="field-detail">
<h5><code>tissue_type_details</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>f551cf87-2c6e-4b92-888d-6310e6a500d8</code></li>
<li><strong>Aliases:</strong> Tissue Type Details</li>
<li><strong>Subsets:</strong> Non-Brain Specimen Collected</li>
</ul>
<p>The details of the non-brain tissue that is available from this organism.</p>
</div>

<div id="tissue_source" class="field-detail">
<h5><code>tissue_source</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>ee83ecf8-4fca-4353-a9ed-4cdd82eb167e</code></li>
<li><strong>Aliases:</strong> Tissue Source</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>The source of the non-brain tissue that is available from this organism.</p>
</div>

<div id="date_of_collection" class="field-detail">
<h5><code>date_of_collection</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>9b94949c-a7c9-4d81-a1c9-a70c96c16ca3</code></li>
<li><strong>Aliases:</strong> Date of Collection</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>The date that the tissue collection occurred.</p>
</div>

<div id="age_at_date_of_collection" class="field-detail">
<h5><code>age_at_date_of_collection</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>6c53ac16-fe2d-48d7-b3d4-b8946b5d2547</code></li>
<li><strong>Aliases:</strong> Age at Date of Collection</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
<li><strong>Range:</strong> 0 – 999 year</li>
</ul>
<p>The age of the donor at the date of tissue collection (years).</p>
</div>

<div id="clinical_brain_diagnosis" class="field-detail">
<h5><code>clinical_brain_diagnosis</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b49f026b-4f6c-48c8-b170-bf6d24c672ef</code></li>
<li><strong>Aliases:</strong> Clinical Brain Diagnosis Available</li>
<li><strong>Subsets:</strong> Diagnoses</li>
</ul>
<p>The status (available/unavailable) of the clinical brain diagnosis of the donor.</p>
</div>

<div id="clinical_brain_diagnosis_code" class="field-detail">
<h5><code>clinical_brain_diagnosis_code</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b7a34c73-ae08-43d3-80d2-d5ef8436e449</code></li>
<li><strong>Aliases:</strong> Clinical Brain Diagnosis Code</li>
<li><strong>Subsets:</strong> Diagnoses</li>
</ul>
<p>The code of the donor&#x27;s clinical brain diagnosis.</p>
</div>

<div id="clinical_brain_diagnosis_confidence_level" class="field-detail">
<h5><code>clinical_brain_diagnosis_confidence_level</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>2e72b4b9-d5fb-4f0d-897c-1f977ed4fabd</code></li>
<li><strong>Aliases:</strong> Clinical Brain Diagnosis Confidence Level</li>
<li><strong>Subsets:</strong> Diagnoses</li>
</ul>
<p>The confidence level of the donor&#x27;s clinical brain diagnosis.</p>
</div>

<div id="genetic_diagnosis" class="field-detail">
<h5><code>genetic_diagnosis</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>f67d3837-159d-4868-9749-aa6c83ded7eb</code></li>
<li><strong>Aliases:</strong> Genetic Diagnosis Available</li>
<li><strong>Subsets:</strong> Diagnoses</li>
</ul>
<p>The status (available, unavailable) of the genetic diagnosis of the donor.</p>
</div>

<div id="genetic_diagnosis_code" class="field-detail">
<h5><code>genetic_diagnosis_code</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>7a7916e0-ff79-4426-b49f-58e2f2a8a367</code></li>
<li><strong>Aliases:</strong> Genetic Diagnosis Code</li>
<li><strong>Subsets:</strong> Diagnoses</li>
</ul>
<p>The code of the donor&#x27;s genetic diagnosis.</p>
</div>

<div id="genetic_diagnosis_confidence_level" class="field-detail">
<h5><code>genetic_diagnosis_confidence_level</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>cb2b0108-8c07-40e8-92a3-b693b6dc64b4</code></li>
<li><strong>Aliases:</strong> Genetic Diagnosis Confidence Level</li>
<li><strong>Subsets:</strong> Diagnoses</li>
</ul>
<p>The confidence level of the donor&#x27;s genetic diagnosis.</p>
</div>

<div id="non_brain_diagnosis" class="field-detail">
<h5><code>non_brain_diagnosis</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>009ec58e-32e4-4712-930c-056e72c8d8fa</code></li>
<li><strong>Aliases:</strong> Non Brain Diagnosis Available</li>
<li><strong>Subsets:</strong> Diagnoses</li>
</ul>
<p>The status (available, unavailable) of a non-brain diagnosis of the donor.</p>
</div>

<div id="non_brain_diagnosis_code" class="field-detail">
<h5><code>non_brain_diagnosis_code</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>65e8824e-01d2-44cf-9f47-9962461a65c9</code></li>
<li><strong>Aliases:</strong> Non Brain Diagnosis Code</li>
<li><strong>Subsets:</strong> Diagnoses</li>
</ul>
<p>The code of the donor&#x27;s non-brain diagnosis.</p>
</div>

<div id="non_brain_diagnosis_confidence_level" class="field-detail">
<h5><code>non_brain_diagnosis_confidence_level</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>2a7ff937-287b-40a3-a1f6-ebf598683774</code></li>
<li><strong>Aliases:</strong> Non Brain Diagnosis Confidence Level</li>
<li><strong>Subsets:</strong> Diagnoses</li>
</ul>
<p>The confidence level of the donor&#x27;s non-brain diagnosis.</p>
</div>

<div id="birth_weight_lbs" class="field-detail">
<h5><code>birth_weight_lbs</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>69d9a60d-32d5-4c3a-a26a-802d8f030c8d</code></li>
<li><strong>Aliases:</strong> Birth Weight Value (lbs)</li>
<li><strong>Subsets:</strong> Infant Medical History</li>
<li><strong>Range:</strong> 0 – 100 pound</li>
</ul>
<p>The weight (at birth) of the subject/donor in pounds.</p>
</div>

<div id="birth_weight_oz" class="field-detail">
<h5><code>birth_weight_oz</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b6f30050-f762-4427-8533-31738e737ea2</code></li>
<li><strong>Aliases:</strong> Birth Weight Value (oz)</li>
<li><strong>Subsets:</strong> Infant Medical History</li>
<li><strong>Range:</strong> 0 – 100 ounce</li>
</ul>
<p>The weight (at birth) of the subject/donor in ounces.</p>
</div>

<div id="gestational_age_value_weeks" class="field-detail">
<h5><code>gestational_age_value_weeks</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>6d8a9b3f-792c-48c2-bd3c-56e52bb51672</code></li>
<li><strong>Aliases:</strong> Gestational Age Value (weeks)</li>
<li><strong>Subsets:</strong> Infant Medical History</li>
<li><strong>Range:</strong> 1 – 45 week</li>
</ul>
<p>The gestational age of the subject/donor in weeks.</p>
</div>

<div id="gestational_age_value_days" class="field-detail">
<h5><code>gestational_age_value_days</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>4e532e52-6e4c-46cd-9fde-96f97ef3b034</code></li>
<li><strong>Aliases:</strong> Gestational Age Value (days)</li>
<li><strong>Subsets:</strong> Infant Medical History</li>
<li><strong>Range:</strong> 0 – 6 day</li>
</ul>
<p>The gestational age of the subject/donor in days.</p>
</div>

<div id="apgar_5_minute_score_available" class="field-detail">
<h5><code>apgar_5_minute_score_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>e67d93ac-3753-4835-a250-e2ca207b2675</code></li>
<li><strong>Aliases:</strong> APGAR Five Minute Score Available</li>
<li><strong>Subsets:</strong> Infant Medical History</li>
</ul>
<p>The status (available, unavailable) of a five-minute APGAR score of the donor.</p>
</div>

<div id="apgar_5_minute_score" class="field-detail">
<h5><code>apgar_5_minute_score</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>3a10dabf-39b0-4eb7-8399-85fd325c5646</code></li>
<li><strong>Aliases:</strong> APGAR Five Minute Score</li>
<li><strong>Subsets:</strong> Infant Medical History</li>
<li><strong>Range:</strong> 1 – 10</li>
</ul>
<p>The score of the donor&#x27;s five-minute APGAR.</p>
</div>

<div id="apgar_10_minute_score_available" class="field-detail">
<h5><code>apgar_10_minute_score_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>3d085ff9-7034-487d-a2b2-b9ae80d55333</code></li>
<li><strong>Aliases:</strong> APGAR Ten Minute Score Available</li>
<li><strong>Subsets:</strong> Infant Medical History</li>
</ul>
<p>The status (available, unavailable) of a ten-minute APGAR score of the donor.</p>
</div>

<div id="apgar_10_minute_score" class="field-detail">
<h5><code>apgar_10_minute_score</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>09d512b6-7c20-4693-8894-77824ad7f04d</code></li>
<li><strong>Aliases:</strong> APGAR Ten Minute Score</li>
<li><strong>Subsets:</strong> Infant Medical History</li>
<li><strong>Range:</strong> 1 – 10</li>
</ul>
<p>The score of the donor&#x27;s ten-minute APGAR.</p>
</div>

<div id="perinatal_neurologic_event_type" class="field-detail">
<h5><code>perinatal_neurologic_event_type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>cb4c7e3b-73fc-400e-a4c3-b149a5544363</code></li>
<li><strong>Aliases:</strong> Perinatal Neurologic Event Type</li>
<li><strong>Subsets:</strong> Perinatal Neurologic Events</li>
</ul>
<p>The perinatal neurologic event of a donor.</p>
</div>

<div id="perinatal_neurologic_event_type_specify" class="field-detail">
<h5><code>perinatal_neurologic_event_type_specify</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>1bf1f9c5-79a6-4203-910f-cad79fe9cac9</code></li>
<li><strong>Aliases:</strong> Perinatal Neurologic Event Type Specify</li>
<li><strong>Subsets:</strong> Perinatal Neurologic Events</li>
</ul>
<p>The specific perinatal neurologic event of a donor.</p>
</div>

<div id="family_history_available" class="field-detail">
<h5><code>family_history_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>c88bf4dc-5a7c-4f70-a773-e6bbb5a12ec9</code></li>
<li><strong>Aliases:</strong> Family History Available</li>
<li><strong>Subsets:</strong> Family History</li>
</ul>
<p>The status (available, unavailable) of the family history of the subject/donor.</p>
</div>

<div id="relative_type" class="field-detail">
<h5><code>relative_type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>1adef34c-bb96-4dd0-bc87-51868f2ddc3f</code></li>
<li><strong>Aliases:</strong> Relative Type</li>
<li><strong>Subsets:</strong> Family History</li>
</ul>
<p>The familial relation to the subject/donor.</p>
</div>

<div id="relative_type_specify" class="field-detail">
<h5><code>relative_type_specify</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>094064a1-362c-4b75-8556-6b874c843fdb</code></li>
<li><strong>Aliases:</strong> Relative Type Specify</li>
<li><strong>Subsets:</strong> Family History</li>
</ul>
<p>The specific familial relation to the subject/donor.</p>
</div>

<div id="condition_type" class="field-detail">
<h5><code>condition_type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>030c8275-04c0-4e4f-9f68-48fd0f559250</code></li>
<li><strong>Aliases:</strong> Condition Type</li>
<li><strong>Subsets:</strong> Family History</li>
</ul>
<p>A condition of the donor.</p>
</div>

<div id="condition_type_specify" class="field-detail">
<h5><code>condition_type_specify</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>a1ed23dc-3cd5-41c8-87f6-58604fc66a70</code></li>
<li><strong>Aliases:</strong> Condition Type Specify</li>
<li><strong>Subsets:</strong> Family History</li>
</ul>
<p>A specific type of condition of a donor.</p>
</div>

<div id="test_name" class="field-detail">
<h5><code>test_name</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b6865e15-7538-4890-be99-a6f9e9920af3</code></li>
<li><strong>Aliases:</strong> Test Name</li>
<li><strong>Subsets:</strong> Infectious Disease Testing</li>
</ul>
<p>The name of the test that has been performed.</p>
</div>

<div id="test_result" class="field-detail">
<h5><code>test_result</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>c14ea006-662c-4666-bfd1-6ff580c403ed</code></li>
<li><strong>Aliases:</strong> Result</li>
<li><strong>Subsets:</strong> Infectious Disease Testing</li>
</ul>
<p>The result(s) of the test that has been performed.</p>
</div>

<div id="tissue_source" class="field-detail">
<h5><code>tissue_source</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>42f8e11b-d9a3-48fe-ac1e-cd6f4469de46</code></li>
<li><strong>Aliases:</strong> Testing Tissue Source</li>
<li><strong>Subsets:</strong> Infectious Disease Testing</li>
</ul>
<p>The tissue sample location or identifier that is the subject of a test.</p>
</div>

<div id="drugs_found" class="field-detail">
<h5><code>drugs_found</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>e35b53f1-0daa-4b5b-9246-cfba52f61bfb</code></li>
<li><strong>Aliases:</strong> Drugs Found</li>
<li><strong>Subsets:</strong> Toxicology Screening</li>
</ul>
<p>A list of drugs found present in a donor.</p>
</div>

<div id="drugs_found_specify" class="field-detail">
<h5><code>drugs_found_specify</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>ec3f7c47-9062-4b66-ba80-a9355a388bc0</code></li>
<li><strong>Aliases:</strong> Drugs Found Specify</li>
<li><strong>Subsets:</strong> Toxicology Screening</li>
</ul>
<p>A list of specific drugs found present in a donor.</p>
</div>

<div id="toxicology_result" class="field-detail">
<h5><code>toxicology_result</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>2cf1a1af-1ece-4ef7-b513-e4d1949f237c</code></li>
<li><strong>Aliases:</strong> Toxicology Result</li>
<li><strong>Subsets:</strong> Toxicology Screening</li>
</ul>
<p>The toxicology result of the donor.</p>
</div>

<div id="toxicology_report_level" class="field-detail">
<h5><code>toxicology_report_level</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>594179b0-c744-40a4-958d-fc81461b4b74</code></li>
<li><strong>Aliases:</strong> Toxicology Report level</li>
<li><strong>Subsets:</strong> Toxicology Screening</li>
</ul>
<p>The report level of the toxicology result of the donor.</p>
</div>

<div id="toxicology_units" class="field-detail">
<h5><code>toxicology_units</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>6f124149-50de-489d-b9e2-f198b2b9857d</code></li>
<li><strong>Aliases:</strong> Toxicology Units</li>
<li><strong>Subsets:</strong> Toxicology Screening</li>
</ul>
<p>The units of the report level of the toxicology result of the donor.</p>
</div>

<div id="artifacts" class="field-detail">
<h5><code>artifacts</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b344b605-21dd-4e06-9104-21005179026f</code></li>
<li><strong>Aliases:</strong> Artifacts</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The neuropathology artifacts available for a donor.</p>
</div>

<div id="artifacts_type" class="field-detail">
<h5><code>artifacts_type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>dc217b9b-ed6b-48e2-93b4-4f648dc395f7</code></li>
<li><strong>Aliases:</strong> Artifacts Type</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The type of neuropathology artifacts available for a donor.</p>
</div>

<div id="artifacts_type_specify" class="field-detail">
<h5><code>artifacts_type_specify</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>ae11485d-dfc6-45fe-9d22-1d0bf7244d7c</code></li>
<li><strong>Aliases:</strong> Artifacts Type Specify</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The specific types of neuropathology artifacts available for a donor.</p>
</div>

<div id="neuropathology_diagnosis" class="field-detail">
<h5><code>neuropathology_diagnosis</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>87f6d251-e028-4480-9272-3497655fb9cd</code></li>
<li><strong>Aliases:</strong> Neuropathology Diagnosis Available</li>
<li><strong>Subsets:</strong> Diagnoses</li>
</ul>
<p>The neuropathology diagnosis of a donor.</p>
</div>

<div id="neuropathology_diagnosis_code" class="field-detail">
<h5><code>neuropathology_diagnosis_code</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>784e9cc1-7258-4535-a6d5-f7f9a4c2da4b</code></li>
<li><strong>Aliases:</strong> Neuorpathology Diagnosis Code</li>
<li><strong>Subsets:</strong> Diagnoses</li>
</ul>
<p>The code of the donor&#x27;s neuropathology diagnosis.</p>
</div>

<div id="developmental" class="field-detail">
<h5><code>developmental</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>c259cdc2-7c68-48de-ab57-57328f3bddfa</code></li>
<li><strong>Aliases:</strong> Developmental</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The type of developmental disorder or disease of a donor.</p>
</div>

<div id="developmental_type_specify" class="field-detail">
<h5><code>developmental_type_specify</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>bee7d477-2dec-4bf5-878e-a105a0054366</code></li>
<li><strong>Aliases:</strong> Developmental Type Specify</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The specific type of developmental disorder or disease of a donor.</p>
</div>

<div id="inflammatory" class="field-detail">
<h5><code>inflammatory</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>05e83583-078d-4a1e-892d-e6f611e5a0b8</code></li>
<li><strong>Aliases:</strong> Inflammatory</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The type of inflammatory disorder or disease of a donor.</p>
</div>

<div id="inflammatory_type_specify" class="field-detail">
<h5><code>inflammatory_type_specify</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>616ba8d8-ced3-4f3e-b1ca-7103eb7a2c94</code></li>
<li><strong>Aliases:</strong> Inflammatory Type Specify</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The specific type of inflammatory disorder or disease of a donor.</p>
</div>

<div id="infectious" class="field-detail">
<h5><code>infectious</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>266f5fb8-716b-4472-be30-4a94b62f2245</code></li>
<li><strong>Aliases:</strong> Infectious</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The type of infectious disease of a donor.</p>
</div>

<div id="infectious_type_specify" class="field-detail">
<h5><code>infectious_type_specify</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>c73cea5e-44d1-4dd9-b55e-3c6ef5dd2ef2</code></li>
<li><strong>Aliases:</strong> Infectious Type Specify</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The specific type of infectious disease of a donor.</p>
</div>

<div id="traumatic" class="field-detail">
<h5><code>traumatic</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>a00497c0-376f-4b2e-b60e-d6add2af41dc</code></li>
<li><strong>Aliases:</strong> Traumatic</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The trauma of a donor.</p>
</div>

<div id="traumatic_type" class="field-detail">
<h5><code>traumatic_type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>01d2f488-f30b-40e0-913f-c9adc6b39b97</code></li>
<li><strong>Aliases:</strong> Traumatic Type</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The type of trauma of a donor.</p>
</div>

<div id="traumatic_type_specify" class="field-detail">
<h5><code>traumatic_type_specify</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>aa574a9a-a3d0-4a07-bf8b-9db4a1110a88</code></li>
<li><strong>Aliases:</strong> Traumatic Type Specify</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The specific type of trauma of a donor.</p>
</div>

<div id="vascular" class="field-detail">
<h5><code>vascular</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b02d8386-d059-42a8-94cb-751d56b15b3a</code></li>
<li><strong>Aliases:</strong> Vascular</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The vascular disease of a donor.</p>
</div>

<div id="vascular_type" class="field-detail">
<h5><code>vascular_type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>5beafa90-ffdb-4cce-a78c-a3b3175210b6</code></li>
<li><strong>Aliases:</strong> Vascular Type</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The type of vascular disease of a donor.</p>
</div>

<div id="vascular_type_specify" class="field-detail">
<h5><code>vascular_type_specify</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>543acbbb-9da4-4e24-a9d7-c0642aa33f32</code></li>
<li><strong>Aliases:</strong> Vascular Type Specify</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The specific type of vascular disease of a donor.</p>
</div>

<div id="neoplastic" class="field-detail">
<h5><code>neoplastic</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>3f52a0e9-6469-46d3-8ed5-3cdb8afdc259</code></li>
<li><strong>Aliases:</strong> Neoplastic</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The neoplastic status of a donor.</p>
</div>

<div id="neoplastic_type" class="field-detail">
<h5><code>neoplastic_type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>a58be8f4-2756-4a66-9d05-1fbf44b4e810</code></li>
<li><strong>Aliases:</strong> Neoplastic Type</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The type of neoplastic status of a donor.</p>
</div>

<div id="neoplastic_type_specify" class="field-detail">
<h5><code>neoplastic_type_specify</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b9e8aead-fdf3-453e-a46b-fcb01d661f8f</code></li>
<li><strong>Aliases:</strong> Neoplastic Type Specify</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The specific type of neoplastic status of a donor.</p>
</div>

<div id="aging" class="field-detail">
<h5><code>aging</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>40e3caa7-657b-4137-9879-07e6b29bae14</code></li>
<li><strong>Aliases:</strong> Aging</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>A developmental process that is a deterioration and loss of function over time. Aging includes loss of functions such as resistance to disease, homeostasis, and fertility, as well as wear and tear. Aging includes cellular senescence, but is more inclusive. May precede death and may succeed developmental maturation.</p>
</div>

<div id="aging_type" class="field-detail">
<h5><code>aging_type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>5e31b66f-131e-4d5e-8760-ddd85f5634d5</code></li>
<li><strong>Aliases:</strong> Aging Type</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The type of aging of a donor.</p>
</div>

<div id="aging_type_specify" class="field-detail">
<h5><code>aging_type_specify</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>8667d972-175c-430a-ac5e-656563e75736</code></li>
<li><strong>Aliases:</strong> Aging Type Specify</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The specific type of aging of a donor.</p>
</div>

<div id="neurodegenerative" class="field-detail">
<h5><code>neurodegenerative</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>764d80ce-7a83-4e68-92df-34a416475e1b</code></li>
<li><strong>Aliases:</strong> Neurodegenerative</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>A disorder of the central nervous system characterized by gradual and progressive loss of neural tissue and neurologic function.</p>
</div>

<div id="neurodegenerative_type" class="field-detail">
<h5><code>neurodegenerative_type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b150b62c-a968-4f5d-9aa3-d1ab5207ff83</code></li>
<li><strong>Aliases:</strong> Neurodegenerative Type</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The type of neurodegenerative disorder of a donor.</p>
</div>

<div id="neurodegenerative_type_specify" class="field-detail">
<h5><code>neurodegenerative_type_specify</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>d422d827-539f-4d10-b09d-0f4be00d7c91</code></li>
<li><strong>Aliases:</strong> Neurodegenerative Type Specify</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The specific type of neurodegenerative disorder of a donor.</p>
</div>

<!-- schema-properties-end -->

## Changelog