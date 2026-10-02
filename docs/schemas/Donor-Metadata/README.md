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

#### Donor

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`donor_nhash_id`](#donor_nhash_id) | text | yes | NHash Donor ID | NIMP generated globally unique identifier for a Donor |
| [`repository`](#repository) | categorical | no | Repository | If the brain is from NBB the NBB repository the brain belongs to |
| [`donor_source`](#donor_source) | categorical | yes | Donor Source | The source of the donor brain e.g. NBB/UM1 project/other |
| [`ethnicity`](#ethnicity) | categorical | no | Ethnicity | Ethnicity of the donor |
| [`race`](#race) | categorical | no | Race | Race of the donor |
| [`secondary_race`](#secondary_race) | categorical | no | Second Race | Second race if available for the donor |
| [`sex`](#sex) | categorical | no | Sex at Birth | Donor&#x27;s sex at birth |
| [`gender`](#gender) | categorical | no | Gender at Time of Death | Donor&#x27;s gender at death |
| [`sex_orientation`](#sex_orientation) | categorical | no | Sexual Orientation at Time of Death | Donor&#x27;s sexual orientation at death |
| [`age_of_death`](#age_of_death) | integer | no | Age Value (Years) | Donor&#x27;s age at death in years |
| [`birth_country_name`](#birth_country_name) | categorical | no | Birth Country Name | Donor&#x27;s birth country |
| [`primary_language`](#primary_language) | categorical | no | Primary Language Code | Donor&#x27;s primary language |
| [`secondary_language`](#secondary_language) | categorical | no | Secondary Language Code | Donor&#x27;s secondary language |
| [`marital_status`](#marital_status) | categorical | no | Marital or Partner Status ATOD | Donor&#x27;s marital or partner status |
| [`education_years_number`](#education_years_number) | integer | no | Education Years Number | Number of years of education the donor had |
| [`handedness`](#handedness) | categorical | no | Handedness | Donor&#x27;s handedness |
| [`confirmed_hbcac`](#confirmed_hbcac) | categorical | no | HBCAC Confirmation Status | Confirmation status of meeting inclusion criteria of the Human Brain Cell Atlas Collection at NBB |
| [`age_at_death_value`](#age_at_death_value) | float | no | Age at Death Value | Donor&#x27;s age at death value |
| [`age_at_death_unit`](#age_at_death_unit) | categorical | no | Age at Death Unit | The unit of the value mentioned under &quot;age_at_death_value&quot; |
| [`age_at_death_reference_point`](#age_at_death_reference_point) | categorical | no | Age at Death Reference Point | Reference point from which the donor&#x27;s age at death was calculated |
| [`donor_species`](#donor_species) | categorical | yes | Donor Species | NCBI Taxonomy code of the donor species |
| [`consent_status`](#consent_status) | categorical | no | Consent Status | Whether the type of consent is open or controlled |
| [`positive_test_result`](#positive_test_result) | categorical | no | The Indicator of Serology Test Positivity | Whether the donor has had a positive serology test result |
| [`access_level`](#access_level) | categorical | no | Access Level |  |
| [`data_use_limitation`](#data_use_limitation) | categorical | no | Data Use Limitation |  |
| [`disease_specification`](#disease_specification) | categorical | no | Disease Specification |  |
| [`irb_approval_required`](#irb_approval_required) | categorical | no | IRB Approval Required |  |
| [`publication_required`](#publication_required) | categorical | no | Publication Required |  |
| [`collaboration_required`](#collaboration_required) | categorical | no | Collaboration Required |  |
| [`not_for_profit`](#not_for_profit) | categorical | no | Not-for-profit Use Only |  |
| [`methods`](#methods) | categorical | no | Methods |  |
| [`genetic_study_only`](#genetic_study_only) | categorical | no | Genetic Study Only |  |
| [`gsr_controlled_access`](#gsr_controlled_access) | categorical | no | Genomic Summary Results (GSR) Controlled Access |  |
| [`donor_project`](#donor_project) | categorical | yes | Donor Project | Donor Project |
| [`donor_labs`](#donor_labs) | categorical | no | Donor Labs | Donor Labs |
| [`death_causes_data_available`](#death_causes_data_available) | categorical | no | Cause Of Death Data Availability | NIMP indicator for availability of the cause of death |
| [`rins_data_available`](#rins_data_available) | categorical | no | Rin Data Availability | NIMP indicator for availability of RNA Integrity Number |
| [`rines_data_available`](#rines_data_available) | categorical | no | Rine Data Availability | NIMP indicator for availability of RNA Integrity Number equivalent |
| [`hemisphere`](#hemisphere) | categorical | no | Hemisphere | Hemisphere of the brain |
| [`post_mortem_interval`](#post_mortem_interval) | float | no | Post Mortem Interval | Post Mortem Interval in hours |
| [`left_hemisphere_preparation`](#left_hemisphere_preparation) | categorical | no | Left Hemisphere Preparation | The method of which the left hemisphere of the brain was prepared |
| [`left_hemisphere_prep_2`](#left_hemisphere_prep_2) | categorical | no | Left Hemisphere Preparation (Second Method) | The second method used to prepare the left hemisphere |
| [`right_hemisphere_preparation`](#right_hemisphere_preparation) | categorical | no | Right Hemisphere Preparation | The method of which the right hemisphere of the brain was prepared |
| [`right_hemisphere_prep_2`](#right_hemisphere_prep_2) | categorical | no | Right Hemisphere Preparation (Second Method) | The second method used to prepare the right hemisphere |
| [`rin`](#rin) | float | no | RIN | RNA Integrity Number |
| [`rine`](#rine) | float | no | RINe | RNA Integrity Number equivalent |
| [`ph`](#ph) | float | no | pH | pH value |
| [`brain_weight`](#brain_weight) | integer | no | Brain Weight Measurement | The weight of the brain in grams |
| [`weighed_type`](#weighed_type) | categorical | no | Brain Tissue Weighed Type | The type of the brain tissue weighed based on the preparation |
| [`photo_2d_available`](#photo_2d_available) | categorical | no | Photo 2d Available | Is a 2D photograph is available? |
| [`scan_3d_available`](#scan_3d_available) | categorical | no | Scan 3d Available | Is a 3D scan is available? |
| [`antemortem_mri_available`](#antemortem_mri_available) | categorical | no | Antemortem MRI Available | Is an Antemortem MRI is available? |
| [`postmortem_mri_available`](#postmortem_mri_available) | categorical | no | Postmortem MRI Available | Is a Postmortem MRI Available |
| [`postmortem_mri_type`](#postmortem_mri_type) | categorical | no | Postmortem MRI Type | The type of postmortem MRI if it is available. |
| [`non_brain_specimen_data_available`](#non_brain_specimen_data_available) | categorical | no | Non-Brain Specimen Data Availability | NIMP indicator for availability of non-brain Specimen data |
| [`neurologic_events_data_available`](#neurologic_events_data_available) | categorical | no | Neurologic Events Data Availability | NIMP indicator for availability of perinatal neurologic events data |
| [`infectious_testings_data_available`](#infectious_testings_data_available) | categorical | no | Infectious Testing Data Availability | NIMP indicator for availability of infectious Disease/Serology testing data |
| [`tox_screening_data_available`](#tox_screening_data_available) | categorical | no | Toxicology Screening Data Availability | NIMP indicator for availability of toxicology screening data |
| [`nn_diagnoses_data_available`](#nn_diagnoses_data_available) | categorical | no | Neurologic And/Or Neuropathologic Diagnoses Data Availability | NIMP indicator for availability of non-neuropathological diagnoses data |
| [`non_brain_tissue_available`](#non_brain_tissue_available) | categorical | no | Non-Brain Tissue Available | Are any non-brain tissues available? |
| [`tissue_type`](#tissue_type) | categorical | no | Tissue Type | The type of non-brain tissues |
| [`clinical_brain_diagnosis`](#clinical_brain_diagnosis) | categorical | no | Clinical Brain Diagnosis Available | Is any clinical brain diagnosis available? |
| [`clinical_brain_diagnosis_confidence_level`](#clinical_brain_diagnosis_confidence_level) | categorical | no | Clinical Brain Diagnosis Confidence Level | The confidence level of the clinical brain diagnosis |
| [`genetic_diagnosis`](#genetic_diagnosis) | categorical | no | Genetic Diagnosis Available | Is any genetic diagnosis available? |
| [`genetic_diagnosis_confidence_level`](#genetic_diagnosis_confidence_level) | categorical | no | Genetic Diagnosis Confidence Level | The confidence level of the genetic diagnosis |
| [`non_brain_diagnosis`](#non_brain_diagnosis) | categorical | no | Non-Brain Diagnosis Available | Is any non-brain diagnosis available? |
| [`non_brain_diagnosis_confidence_level`](#non_brain_diagnosis_confidence_level) | categorical | no | Non-Brain Diagnosis Confidence Level | The confidence level of the non-brain diagnosis |
| [`birth_weight_lbs`](#birth_weight_lbs) | float | no | Birth Weight Value (Lbs) | Birth weight in pounds |
| [`birth_weight_oz`](#birth_weight_oz) | float | no | Birth Weight Value (Oz) | Birth weight in ounces |
| [`apgar_5_minute_score_available`](#apgar_5_minute_score_available) | categorical | no | Apgar Five Minute Score Available | Is the APGAR Five Minute Score available? This is a test given to newborns soon after birth |
| [`apgar_5_minute_score`](#apgar_5_minute_score) | integer | no | Apgar Five Minute Score | The APGAR Five Minute Score. This is a test given to newborns just after birth |
| [`apgar_10_minute_score_available`](#apgar_10_minute_score_available) | categorical | no | Apgar Ten Minute Score Available | Is the APGAR Ten Minute Score Available? This is a test given to newborns just after birth. |
| [`apgar_10_minute_score`](#apgar_10_minute_score) | integer | no | Apgar Ten Minute Score | The APGAR Ten Minute Score. This is a test given to newborns just after birth |
| [`neuropathology_diagnosis`](#neuropathology_diagnosis) | categorical | no | Neuropathology Diagnosis Available | are any neuropathological diagnosis available? |
| [`artifacts`](#artifacts) | categorical | no | Artifacts | Any artifacts available? |
| [`artifacts_type`](#artifacts_type) | categorical | no | Artifacts Type | The type of artifacts |
| [`developmental`](#developmental) | categorical | no | Developmental | Are any developmental neuropathology diagnoses available? |
| [`inflammatory`](#inflammatory) | categorical | no | Inflammatory | Are inflammatory neuropathology diagnoses available? |
| [`infectious`](#infectious) | categorical | no | Infectious | Are infectious neuropathology diagnoses available? |
| [`traumatic`](#traumatic) | categorical | no | Traumatic | Are traumatic neuropathology diagnoses available? |
| [`traumatic_type`](#traumatic_type) | categorical | no | Traumatic Type | The type of traumatic neuropathology diagnosis |
| [`vascular`](#vascular) | categorical | no | Vascular | Are vascular neuropathology diagnoses available? |
| [`vascular_type`](#vascular_type) | categorical | no | Vascular Type | The type of vascular neuropathology diagnosis |
| [`neoplastic`](#neoplastic) | categorical | no | Neoplastic | Are neoplastic neuropathology diagnoses available? |
| [`neoplastic_type`](#neoplastic_type) | categorical | no | Neoplastic Type | The type of neoplastic neuropathology diagnosis |
| [`aging`](#aging) | categorical | no | Aging | Are aging-related neuropathology diagnoses available? |
| [`aging_type`](#aging_type) | categorical | no | Aging Type | The type of aging-related neuropathology diagnosis |
| [`neurodegenerative`](#neurodegenerative) | categorical | no | Neurodegenerative | Are neurodegenerative neuropathology diagnoses available? |
| [`neurodegenerative_type`](#neurodegenerative_type) | categorical | no | Neurodegenerative Type | The type of neurodegenerative neuropathology diagnosis |

#### The LINKML class or data entity (e.g. purple or orange box in the workflow diagram) with which this metadata field is associated

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`Name of metadata field`](#name-of-metadata-field) | Type of values in this field (integer; float; text; date) | no | Aliases for this metadata element in other schemas/resources | A detailed definition for this field |

### Property Details

#### Donor

<div id="donor_nhash_id" class="field-detail">
<h5><code>donor_nhash_id</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>98b28574-f97f-4436-b723-10a6508431b5</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> NHash Donor ID</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>NIMP generated globally unique identifier for a Donor</p>
</div>

<div id="repository" class="field-detail">
<h5><code>repository</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>408682ed-0e27-41e2-b9fa-f05674366d6e</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Repository</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>If the brain is from NBB the NBB repository the brain belongs to</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="donor_source" class="field-detail">
<h5><code>donor_source</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>0d0cf732-0f76-409d-9a73-7a96d829d3d3</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Donor Source</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>The source of the donor brain e.g. NBB/UM1 project/other</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="ethnicity" class="field-detail">
<h5><code>ethnicity</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>918370df-49f6-4361-9c52-f46b16412980</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Ethnicity</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>Ethnicity of the donor</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="race" class="field-detail">
<h5><code>race</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>e515c009-550e-4f9c-b1b6-fc876a6fb2a8</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Race</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>Race of the donor</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="secondary_race" class="field-detail">
<h5><code>secondary_race</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>192fe5b1-c812-4767-86fb-3178f9914705</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Second Race</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>Second race if available for the donor</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="sex" class="field-detail">
<h5><code>sex</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>c819b9d5-2fde-40b2-bf0d-e07b56f96ac9</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Sex at Birth</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>Donor&#x27;s sex at birth</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="gender" class="field-detail">
<h5><code>gender</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>1c71e775-65aa-442b-a392-1cf9a44e326e</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Gender at Time of Death</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>Donor&#x27;s gender at death</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="sex_orientation" class="field-detail">
<h5><code>sex_orientation</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>e47e8a2f-72fb-4036-b288-f4580dc2aa4e</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Sexual Orientation at Time of Death</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>Donor&#x27;s sexual orientation at death</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="age_of_death" class="field-detail">
<h5><code>age_of_death</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>14eb923a-161d-45e2-889d-81fea7b632b6</code></li>
<li><strong>Data Type:</strong> <code>integer</code></li>
<li><strong>Aliases:</strong> Age Value (Years)</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
<li><strong>Range:</strong> 0 – 200 year</li>
</ul>
<p>Donor&#x27;s age at death in years</p>
</div>

<div id="birth_country_name" class="field-detail">
<h5><code>birth_country_name</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>9c27fd29-b512-492f-a32f-b615c7585ff7</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Birth Country Name</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>Donor&#x27;s birth country</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="primary_language" class="field-detail">
<h5><code>primary_language</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>abe9edc7-96ca-4c6a-a1ed-c008548cc373</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Primary Language Code</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>Donor&#x27;s primary language</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="secondary_language" class="field-detail">
<h5><code>secondary_language</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>37b7495f-b010-4d1c-ae32-9cb19c680950</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Secondary Language Code</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>Donor&#x27;s secondary language</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="marital_status" class="field-detail">
<h5><code>marital_status</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>4f0e41c9-dd15-4a37-ae6b-11b7131d7cba</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Marital or Partner Status ATOD</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>Donor&#x27;s marital or partner status</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="education_years_number" class="field-detail">
<h5><code>education_years_number</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>add3f7fe-ae60-4cc1-bb2e-72bbbe9a1a7d</code></li>
<li><strong>Data Type:</strong> <code>integer</code></li>
<li><strong>Aliases:</strong> Education Years Number</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
<li><strong>Range:</strong> 0 – 30 year</li>
</ul>
<p>Number of years of education the donor had</p>
</div>

<div id="handedness" class="field-detail">
<h5><code>handedness</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>82a4087c-d0e3-48ca-8bea-a81eefc683a0</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Handedness</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>Donor&#x27;s handedness</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="confirmed_hbcac" class="field-detail">
<h5><code>confirmed_hbcac</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b6cdddf7-6f0b-4855-a0fa-16c2ab29f219</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> HBCAC Confirmation Status</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>Confirmation status of meeting inclusion criteria of the Human Brain Cell Atlas Collection at NBB</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="age_at_death_value" class="field-detail">
<h5><code>age_at_death_value</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>57e24d3c-c9c7-4ef3-9809-a35802d563ec</code></li>
<li><strong>Data Type:</strong> <code>float</code></li>
<li><strong>Aliases:</strong> Age at Death Value</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>Donor&#x27;s age at death value</p>
</div>

<div id="age_at_death_unit" class="field-detail">
<h5><code>age_at_death_unit</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b5436e99-f0a7-4c30-825d-56b88ee2ac1d</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Age at Death Unit</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>The unit of the value mentioned under &quot;age_at_death_value&quot;</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="age_at_death_reference_point" class="field-detail">
<h5><code>age_at_death_reference_point</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>3bed1f94-9d82-4ed7-afdf-79d896b24dbb</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Age at Death Reference Point</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>Reference point from which the donor&#x27;s age at death was calculated</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="donor_species" class="field-detail">
<h5><code>donor_species</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>6837cb02-6bd7-4fb8-838c-9062ead96ba4</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Donor Species</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>NCBI Taxonomy code of the donor species</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="consent_status" class="field-detail">
<h5><code>consent_status</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>1a53e733-276f-421a-850d-eb46e50db972</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Consent Status</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>Whether the type of consent is open or controlled</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="positive_test_result" class="field-detail">
<h5><code>positive_test_result</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>0ef73629-5172-4517-a1f8-295be1603b80</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> The Indicator of Serology Test Positivity</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>Whether the donor has had a positive serology test result</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="access_level" class="field-detail">
<h5><code>access_level</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>60794406-316a-419b-98a7-5ea49f55392e</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Access Level</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p></p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="data_use_limitation" class="field-detail">
<h5><code>data_use_limitation</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>aea2f9a4-ebc7-4dc6-97d3-cb517774966d</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Data Use Limitation</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p></p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="disease_specification" class="field-detail">
<h5><code>disease_specification</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>47003dfa-c6a0-4302-998b-0be0fb64261f</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Disease Specification</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p></p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="irb_approval_required" class="field-detail">
<h5><code>irb_approval_required</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>71ccc15c-0983-420b-9301-ad79d8372ff1</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> IRB Approval Required</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p></p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="publication_required" class="field-detail">
<h5><code>publication_required</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>7eb1e5a1-a2f5-4ec7-aef3-e2d56ed56a6f</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Publication Required</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p></p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="collaboration_required" class="field-detail">
<h5><code>collaboration_required</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>95f7b929-6a9f-496d-9512-693397f48dad</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Collaboration Required</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p></p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="not_for_profit" class="field-detail">
<h5><code>not_for_profit</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>0dc07cdf-93a7-445b-9555-17d0249fe349</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Not-for-profit Use Only</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p></p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="methods" class="field-detail">
<h5><code>methods</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>97ade474-302f-4f56-bad9-603c28a2a721</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Methods</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p></p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="genetic_study_only" class="field-detail">
<h5><code>genetic_study_only</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>f7935a44-f816-4a61-ab57-96439447c63a</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Genetic Study Only</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p></p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="gsr_controlled_access" class="field-detail">
<h5><code>gsr_controlled_access</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>3bb3bf75-ec1d-4ab7-a6a4-28d9da85f948</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Genomic Summary Results (GSR) Controlled Access</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p></p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="donor_project" class="field-detail">
<h5><code>donor_project</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>cd772fb0-a2fe-4df3-b2dd-b62370be37fc</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Donor Project</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>Donor Project</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="donor_labs" class="field-detail">
<h5><code>donor_labs</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b97c384f-a556-42a2-a3c2-c31e5771f481</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Donor Labs</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>Donor Labs</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="death_causes_data_available" class="field-detail">
<h5><code>death_causes_data_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>e46e9d58-d982-4800-b7de-67f608951211</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Cause Of Death Data Availability</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>NIMP indicator for availability of the cause of death</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="rins_data_available" class="field-detail">
<h5><code>rins_data_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>d05825e6-b785-42a3-9bdf-c34b30e698b8</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Rin Data Availability</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>NIMP indicator for availability of RNA Integrity Number</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="rines_data_available" class="field-detail">
<h5><code>rines_data_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>28a5e912-570b-4a7f-87f2-36bd5db92090</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Rine Data Availability</li>
<li><strong>Subsets:</strong> General Subject Fields</li>
</ul>
<p>NIMP indicator for availability of RNA Integrity Number equivalent</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="hemisphere" class="field-detail">
<h5><code>hemisphere</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>68b7a28b-d695-4ec9-800b-6a27ca206081</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Hemisphere</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>Hemisphere of the brain</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="post_mortem_interval" class="field-detail">
<h5><code>post_mortem_interval</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>6fd5c5ac-b128-4a4a-ae98-09eaeba22f92</code></li>
<li><strong>Data Type:</strong> <code>float</code></li>
<li><strong>Aliases:</strong> Post Mortem Interval</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
<li><strong>Range:</strong> 0 – 8888 hour</li>
</ul>
<p>Post Mortem Interval in hours</p>
</div>

<div id="left_hemisphere_preparation" class="field-detail">
<h5><code>left_hemisphere_preparation</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>57d5378f-a451-4bf5-a472-cc88d0d29586</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Left Hemisphere Preparation</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>The method of which the left hemisphere of the brain was prepared</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="left_hemisphere_prep_2" class="field-detail">
<h5><code>left_hemisphere_prep_2</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>d76753fb-b30b-419b-b853-d341510d8034</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Left Hemisphere Preparation (Second Method)</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>The second method used to prepare the left hemisphere</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="right_hemisphere_preparation" class="field-detail">
<h5><code>right_hemisphere_preparation</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>477c2600-f979-43c5-9c61-ab61fd771584</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Right Hemisphere Preparation</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>The method of which the right hemisphere of the brain was prepared</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="right_hemisphere_prep_2" class="field-detail">
<h5><code>right_hemisphere_prep_2</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b0a52336-fe31-4ac4-8914-b0bb76a8ef5a</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Right Hemisphere Preparation (Second Method)</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>The second method used to prepare the right hemisphere</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="rin" class="field-detail">
<h5><code>rin</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>cd472c0d-0b64-45c9-a38e-e54d15cea953</code></li>
<li><strong>Data Type:</strong> <code>float</code></li>
<li><strong>Aliases:</strong> RIN</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
<li><strong>Range:</strong> 0 – 99</li>
</ul>
<p>RNA Integrity Number</p>
</div>

<div id="rine" class="field-detail">
<h5><code>rine</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>1210148d-d8fb-45aa-b51a-4b19b6d09bec</code></li>
<li><strong>Data Type:</strong> <code>float</code></li>
<li><strong>Aliases:</strong> RINe</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
<li><strong>Range:</strong> 0 – 99</li>
</ul>
<p>RNA Integrity Number equivalent</p>
</div>

<div id="ph" class="field-detail">
<h5><code>ph</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>9e67af02-c081-43e1-a42c-bf9603cae616</code></li>
<li><strong>Data Type:</strong> <code>float</code></li>
<li><strong>Aliases:</strong> pH</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
<li><strong>Range:</strong> 0 – 99</li>
</ul>
<p>pH value</p>
</div>

<div id="brain_weight" class="field-detail">
<h5><code>brain_weight</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>546fc32d-f8a2-4c00-924a-8c4730f11f51</code></li>
<li><strong>Data Type:</strong> <code>integer</code></li>
<li><strong>Aliases:</strong> Brain Weight Measurement</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
<li><strong>Range:</strong> 0 – 9998 gram</li>
</ul>
<p>The weight of the brain in grams</p>
</div>

<div id="weighed_type" class="field-detail">
<h5><code>weighed_type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>a7463e3f-0c61-4718-a7d0-60fd2116908a</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Brain Tissue Weighed Type</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>The type of the brain tissue weighed based on the preparation</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="photo_2d_available" class="field-detail">
<h5><code>photo_2d_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>611beda8-1ac6-4183-a284-04a30bb474f3</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Photo 2d Available</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>Is a 2D photograph is available?</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="scan_3d_available" class="field-detail">
<h5><code>scan_3d_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>658e8a80-e232-438f-8c1e-d5f38724dc55</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Scan 3d Available</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>Is a 3D scan is available?</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="antemortem_mri_available" class="field-detail">
<h5><code>antemortem_mri_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>43a04caa-4f28-47ac-8a9d-74c40f10776f</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Antemortem MRI Available</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>Is an Antemortem MRI is available?</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="postmortem_mri_available" class="field-detail">
<h5><code>postmortem_mri_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>0badd072-0c25-48c6-9357-44d5b5bc0818</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Postmortem MRI Available</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>Is a Postmortem MRI Available</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="postmortem_mri_type" class="field-detail">
<h5><code>postmortem_mri_type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>64a607a9-21e6-4c73-8f2e-2d67b0dc51c8</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Postmortem MRI Type</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>The type of postmortem MRI if it is available.</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="non_brain_specimen_data_available" class="field-detail">
<h5><code>non_brain_specimen_data_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>e537aacd-040a-423b-9920-9ce5adecf111</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Non-Brain Specimen Data Availability</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>NIMP indicator for availability of non-brain Specimen data</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="neurologic_events_data_available" class="field-detail">
<h5><code>neurologic_events_data_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>27a7df05-5aec-4060-85b9-2b4658ecd1e8</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Neurologic Events Data Availability</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>NIMP indicator for availability of perinatal neurologic events data</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="infectious_testings_data_available" class="field-detail">
<h5><code>infectious_testings_data_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>af034af4-9a8d-49ed-a100-1e87ebe962f5</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Infectious Testing Data Availability</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>NIMP indicator for availability of infectious Disease/Serology testing data</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="tox_screening_data_available" class="field-detail">
<h5><code>tox_screening_data_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>3730c096-5524-43f4-a3c0-010ccdf80ae1</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Toxicology Screening Data Availability</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>NIMP indicator for availability of toxicology screening data</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="nn_diagnoses_data_available" class="field-detail">
<h5><code>nn_diagnoses_data_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>87a4e421-4586-4938-91cc-6ae4e6e95dde</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Neurologic And/Or Neuropathologic Diagnoses Data Availability</li>
<li><strong>Subsets:</strong> General Specimen Data</li>
</ul>
<p>NIMP indicator for availability of non-neuropathological diagnoses data</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="non_brain_tissue_available" class="field-detail">
<h5><code>non_brain_tissue_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>3a064c96-a956-4cf3-8b77-056b8e392f99</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Non-Brain Tissue Available</li>
<li><strong>Subsets:</strong> Non-Brain Specimen Collected</li>
</ul>
<p>Are any non-brain tissues available?</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="tissue_type" class="field-detail">
<h5><code>tissue_type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>33ccbc85-ae35-44d6-8bc6-c2fb91116cf7</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Tissue Type</li>
<li><strong>Subsets:</strong> Non-Brain Specimen Collected</li>
</ul>
<p>The type of non-brain tissues</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="clinical_brain_diagnosis" class="field-detail">
<h5><code>clinical_brain_diagnosis</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b49f026b-4f6c-48c8-b170-bf6d24c672ef</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Clinical Brain Diagnosis Available</li>
<li><strong>Subsets:</strong> Diagnoses</li>
</ul>
<p>Is any clinical brain diagnosis available?</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="clinical_brain_diagnosis_confidence_level" class="field-detail">
<h5><code>clinical_brain_diagnosis_confidence_level</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>2e72b4b9-d5fb-4f0d-897c-1f977ed4fabd</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Clinical Brain Diagnosis Confidence Level</li>
<li><strong>Subsets:</strong> Diagnoses</li>
</ul>
<p>The confidence level of the clinical brain diagnosis</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="genetic_diagnosis" class="field-detail">
<h5><code>genetic_diagnosis</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>f67d3837-159d-4868-9749-aa6c83ded7eb</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Genetic Diagnosis Available</li>
<li><strong>Subsets:</strong> Diagnoses</li>
</ul>
<p>Is any genetic diagnosis available?</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="genetic_diagnosis_confidence_level" class="field-detail">
<h5><code>genetic_diagnosis_confidence_level</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>cb2b0108-8c07-40e8-92a3-b693b6dc64b4</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Genetic Diagnosis Confidence Level</li>
<li><strong>Subsets:</strong> Diagnoses</li>
</ul>
<p>The confidence level of the genetic diagnosis</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="non_brain_diagnosis" class="field-detail">
<h5><code>non_brain_diagnosis</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>009ec58e-32e4-4712-930c-056e72c8d8fa</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Non-Brain Diagnosis Available</li>
<li><strong>Subsets:</strong> Diagnoses</li>
</ul>
<p>Is any non-brain diagnosis available?</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="non_brain_diagnosis_confidence_level" class="field-detail">
<h5><code>non_brain_diagnosis_confidence_level</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>2a7ff937-287b-40a3-a1f6-ebf598683774</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Non-Brain Diagnosis Confidence Level</li>
<li><strong>Subsets:</strong> Diagnoses</li>
</ul>
<p>The confidence level of the non-brain diagnosis</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="birth_weight_lbs" class="field-detail">
<h5><code>birth_weight_lbs</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>69d9a60d-32d5-4c3a-a26a-802d8f030c8d</code></li>
<li><strong>Data Type:</strong> <code>float</code></li>
<li><strong>Aliases:</strong> Birth Weight Value (Lbs)</li>
<li><strong>Subsets:</strong> Infant Medical History</li>
<li><strong>Range:</strong> 0 – 100 pound</li>
</ul>
<p>Birth weight in pounds</p>
</div>

<div id="birth_weight_oz" class="field-detail">
<h5><code>birth_weight_oz</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b6f30050-f762-4427-8533-31738e737ea2</code></li>
<li><strong>Data Type:</strong> <code>float</code></li>
<li><strong>Aliases:</strong> Birth Weight Value (Oz)</li>
<li><strong>Subsets:</strong> Infant Medical History</li>
<li><strong>Range:</strong> 0 – 100 ounce</li>
</ul>
<p>Birth weight in ounces</p>
</div>

<div id="apgar_5_minute_score_available" class="field-detail">
<h5><code>apgar_5_minute_score_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>e67d93ac-3753-4835-a250-e2ca207b2675</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Apgar Five Minute Score Available</li>
<li><strong>Subsets:</strong> Infant Medical History</li>
</ul>
<p>Is the APGAR Five Minute Score available? This is a test given to newborns soon after birth</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="apgar_5_minute_score" class="field-detail">
<h5><code>apgar_5_minute_score</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>3a10dabf-39b0-4eb7-8399-85fd325c5646</code></li>
<li><strong>Data Type:</strong> <code>integer</code></li>
<li><strong>Aliases:</strong> Apgar Five Minute Score</li>
<li><strong>Subsets:</strong> Infant Medical History</li>
<li><strong>Range:</strong> 1 – 10</li>
</ul>
<p>The APGAR Five Minute Score. This is a test given to newborns just after birth</p>
</div>

<div id="apgar_10_minute_score_available" class="field-detail">
<h5><code>apgar_10_minute_score_available</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>3d085ff9-7034-487d-a2b2-b9ae80d55333</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Apgar Ten Minute Score Available</li>
<li><strong>Subsets:</strong> Infant Medical History</li>
</ul>
<p>Is the APGAR Ten Minute Score Available? This is a test given to newborns just after birth.</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="apgar_10_minute_score" class="field-detail">
<h5><code>apgar_10_minute_score</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>09d512b6-7c20-4693-8894-77824ad7f04d</code></li>
<li><strong>Data Type:</strong> <code>integer</code></li>
<li><strong>Aliases:</strong> Apgar Ten Minute Score</li>
<li><strong>Subsets:</strong> Infant Medical History</li>
<li><strong>Range:</strong> 1 – 10</li>
</ul>
<p>The APGAR Ten Minute Score. This is a test given to newborns just after birth</p>
</div>

<div id="neuropathology_diagnosis" class="field-detail">
<h5><code>neuropathology_diagnosis</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>87f6d251-e028-4480-9272-3497655fb9cd</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Neuropathology Diagnosis Available</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>are any neuropathological diagnosis available?</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="artifacts" class="field-detail">
<h5><code>artifacts</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b344b605-21dd-4e06-9104-21005179026f</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Artifacts</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>Any artifacts available?</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="artifacts_type" class="field-detail">
<h5><code>artifacts_type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>dc217b9b-ed6b-48e2-93b4-4f648dc395f7</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Artifacts Type</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The type of artifacts</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="developmental" class="field-detail">
<h5><code>developmental</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>c259cdc2-7c68-48de-ab57-57328f3bddfa</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Developmental</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>Are any developmental neuropathology diagnoses available?</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="inflammatory" class="field-detail">
<h5><code>inflammatory</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>05e83583-078d-4a1e-892d-e6f611e5a0b8</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Inflammatory</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>Are inflammatory neuropathology diagnoses available?</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="infectious" class="field-detail">
<h5><code>infectious</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>266f5fb8-716b-4472-be30-4a94b62f2245</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Infectious</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>Are infectious neuropathology diagnoses available?</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="traumatic" class="field-detail">
<h5><code>traumatic</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>a00497c0-376f-4b2e-b60e-d6add2af41dc</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Traumatic</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>Are traumatic neuropathology diagnoses available?</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="traumatic_type" class="field-detail">
<h5><code>traumatic_type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>01d2f488-f30b-40e0-913f-c9adc6b39b97</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Traumatic Type</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The type of traumatic neuropathology diagnosis</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="vascular" class="field-detail">
<h5><code>vascular</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b02d8386-d059-42a8-94cb-751d56b15b3a</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Vascular</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>Are vascular neuropathology diagnoses available?</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="vascular_type" class="field-detail">
<h5><code>vascular_type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>5beafa90-ffdb-4cce-a78c-a3b3175210b6</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Vascular Type</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The type of vascular neuropathology diagnosis</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="neoplastic" class="field-detail">
<h5><code>neoplastic</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>3f52a0e9-6469-46d3-8ed5-3cdb8afdc259</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Neoplastic</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>Are neoplastic neuropathology diagnoses available?</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="neoplastic_type" class="field-detail">
<h5><code>neoplastic_type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>a58be8f4-2756-4a66-9d05-1fbf44b4e810</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Neoplastic Type</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The type of neoplastic neuropathology diagnosis</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="aging" class="field-detail">
<h5><code>aging</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>40e3caa7-657b-4137-9879-07e6b29bae14</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Aging</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>Are aging-related neuropathology diagnoses available?</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="aging_type" class="field-detail">
<h5><code>aging_type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>5e31b66f-131e-4d5e-8760-ddd85f5634d5</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Aging Type</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The type of aging-related neuropathology diagnosis</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="neurodegenerative" class="field-detail">
<h5><code>neurodegenerative</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>764d80ce-7a83-4e68-92df-34a416475e1b</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Neurodegenerative</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>Are neurodegenerative neuropathology diagnoses available?</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

<div id="neurodegenerative_type" class="field-detail">
<h5><code>neurodegenerative_type</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b150b62c-a968-4f5d-9aa3-d1ab5207ff83</code></li>
<li><strong>Data Type:</strong> <code>categorical</code></li>
<li><strong>Aliases:</strong> Neurodegenerative Type</li>
<li><strong>Subsets:</strong> Neuropathological Diagnoses</li>
</ul>
<p>The type of neurodegenerative neuropathology diagnosis</p>
<p><strong>Permissible values:</strong> <code>Yes</code></p>
</div>

#### The LINKML class or data entity (e.g. purple or orange box in the workflow diagram) with which this metadata field is associated

<div id="name-of-metadata-field" class="field-detail">
<h5><code>Name of metadata field</code> <em>(optional)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>UUID of field in BICAN Ecosystem</code></li>
<li><strong>Data Type:</strong> <code>Type of values in this field (integer; float; text; date)</code></li>
<li><strong>Aliases:</strong> Aliases for this metadata element in other schemas/resources</li>
<li><strong>Subsets:</strong> Data use subset for this field</li>
<li><strong>Range:</strong> For measurements if applicable – For measurements if applicable For measurements if applicable</li>
</ul>
<p>A detailed definition for this field</p>
<p><strong>Permissible values:</strong> <code>For fields that have values from a limited set; see Controlled Values table for entries</code></p>
</div>

<!-- schema-properties-end -->

## Changelog