# BICAN Developing Tissue Metadata Schema

Document Status: _Approved by MOWG_

Version: 1.0

Owner: HMBA

Reviewers: @MariahKenney, @licongcui, @patrick-lloyd-ray

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: 08-07-2024

## Background

The Brain Research Through Advancing Innovative Neurotechnologies® (BRAIN) Initiative Cell Atlas Network (BICAN) aims to transform our understanding of brain cell types and the precise tools needed to access them, bringing us one step closer to unraveling the complex workings of the human brain.

Building on findings from the BRAIN Initiative Cell Census Network (BICCN), BICAN takes the next step in mapping brain cells and circuits across multiple species, with an emphasis on humans. The aim of BICAN is to generate a complete reference atlas of cell types in the human brain across the lifespan, which can be shared and used throughout the research community. In addition to developing a “parts list” detailing the vast array of neurons and non-neuronal cells in the human brain, the project also aims to map cell interactions that underlie a wide range of brain disorders.

To this end, BICAN aims to support the publication, sharing, and exploration of datasets generated in the course of the project. Creating a complete reference atlas from multiple datasets requires vast harmonization of metadata. In order to facilitate the harmonization of metadata, we require datasets include a small set of metadata available from data submitters.

This document describes a schema, a type of contract, that BICAN requires of all donor to alignment datasets to enable searching, filtering, and integration of datasets.

Note that the requirements in the schema are just the minimum required information. Datasets often have additional metadata, which is preserved in datasets submitted to the data archives.

## Overview

The BICAN Developing Human and NHP Tissue Metadata schema describes metadata associated with and produced from the preparation of macaque donor and tissue in the HMBA and BICAN. [more detail needed here]

This document has the following sections:

* [General Requirements](#general-requirements)
* [Developing Tissue](#developing-tissue), which describe the metadata required for whole brain spatial omics experiements.
* [Appendix](#appendix)

## General Requirements

**Organisms**. Data must be from a Metazoan organism and defined in the NCBI organismal classification.

**Redundant Metadata**. It is STRONGLY RECOMMENDED to avoid multiple metadata fields containing identical or similar information.

## Developing Tissue

The data in developing tissue is the metadata essential for developing tissue experiments.

The following tables describe the developing tissue metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:

### region of interest

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>region of interest</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>71611b58-f98e-4a69-ad88-c0029a377cbe</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The brain region, structure, or area from which a brain tissue source derives.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>ROI</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### local donor ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>local donor ID</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>subject_id</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>An identifier that uniquely denotes objects only within the scope of a specific object aggregate and that is not registered in an identifier registry.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### hemisphere

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>hemisphere</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>68b7a28b-d695-4ec9-800b-6a27ca206081</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>hemisphere</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>One of two bilateral, largely symmetrical organ subdivisions within the telencephalon which contain the cerebral cortex and cerebral white matter.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### left hemisphere preparation

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>left hemisphere preparation</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>57d5378f-a451-4bf5-a472-cc88d0d29586</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>left_hemisphere_preparation</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The type of preparation method used for the left hemisphere.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### left hemisphere preparation specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>left hemisphere preparation specify</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>002e915e-01c3-4570-a1f3-76680dcb2c33</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>left_hemisphere_preparation_specify</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Specific details about the type of preparation method used for the left hemisphere.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### left hemisphere tissue inventory

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>left hemisphere tissue inventory</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>05e2821e-e7dc-4e33-94dc-7b55c372e5a0</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The inventory (list) of the tissue samples for a specific left hemisphere specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>left_hemisphere_tissue_inventory</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### left hemisphere tissue sampling history

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>left hemisphere tissue sampling history</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b02f7dd7-4535-4b41-b8df-73786b8983bc</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The history of the tissue sampling for a specific left hemisphere specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>left_hemisphere_tissue_sampling_history</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### right hemisphere preparation

<<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>right hemisphere preparation</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>477c2600-f979-43c5-9c61-ab61fd771584</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>right_hemisphere_preparation</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The type of preparation method used for the right hemisphere.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### right hemisphere preparation specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>right hemisphere preparation specify</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>efd50be4-f7cf-4146-a08e-28f25680728c</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>right_hemisphere_preparation_specify</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Specific details about the type of preparation method used for the right hemisphere.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### right hemisphere tissue inventory

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>right hemisphere tissue inventory</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>8b6b910f-beb7-4e2b-881a-7f862ef5d588</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The inventory (list) of the tissue samples for a specific right hemisphere specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>right_hemisphere_tissue_inventory</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### right hemisphere tissue sampling history

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>right hemisphere tissue sampling history</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>60d2efe0-bf7f-48f7-96fc-71cdf03226dd</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The history of the tissue sampling for a specific right hemisphere specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>right_hemisphere_tissue_sampling_history</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### RIN

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>RIN</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>cd472c0d-0b64-45c9-a38e-e54d15cea953</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The RNA integrity number value of a specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>rin</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### RIN tissue source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>RIN tissue source</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d547ee51-9ec3-489c-8e49-7d8cd94080a8</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The tissue sample location or identifier that is used for calculating the RNA integrity number.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>rin_tissue_source</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### RIN testing organization

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>RIN testing organization</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>cfed831e-9a62-4a32-bf92-532873420eb3</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The organization that determines the RNA integrity number of a sample/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>rin_testing_organization</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### RINe

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>RINe</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>1210148d-d8fb-45aa-b51a-4b19b6d09bec</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>A type of RIN (RNA integrity number) value that represents the relative ratio of the signal in the fast zone to the 18S peak signal fpr a specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>rine</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### RINe tissue source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>RINe tissue source</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>7d5fd9af-82a1-4bdb-a3c6-9225d1717c53</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The tissue sample location or identifier that is used for calculating the RINe number.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>rine_tissue_source</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### RINe testing organization

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>RINe testing organization</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>15a6d162-a3ca-4852-b626-a911c37c04c9</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The organization that determines the RINe number.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>rine_testing_organization</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
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
      <th>BICAN UUID</th>
      <td>9e67af02-c081-43e1-a42c-bf9603cae616</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The value of a measurement of acidity or basicity of a tissue, sample, or specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>ph</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### brain weight measurement

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain weight measurement</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>546fc32d-f8a2-4c00-924a-8c4730f11f51</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The weight of a brain specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_weight</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### brain tissue weighed type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain tissue weighed type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a7463e3f-0c61-4718-a7d0-60fd2116908a</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The state of a brain specimen when it is weighed (fresh, frozen, fixed).</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>weighed_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### photo 2d available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>photo 2d available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>611beda8-1ac6-4183-a284-04a30bb474f3</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (available, unavailable) of two-dimensional photos of a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>photo_2d_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### species

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>species</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d11fb2ce-bfdb-4735-9b17-b6ba606520b1</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The species of a subject/donor/sample/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>species</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### matriline and patriline

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>matriline and patriline</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ae0447a3-0504-43a3-95d5-4248e53d3224</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The relavant matriline and patriline information for a subject/donor/sample/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>family_history</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

## Appendix

<!-- schema-properties-start -->
## Schema properties
*Auto-generated from CSV. Do not edit this section manually.*

**Status:** Accepted by MOWG &middot; **Version:** 1.0.0 &middot; **Date:** 2024-07-08

### Properties

#### Family History

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`matriline and patriline`](#matriline-and-patriline) | text | yes | family_history | The relavant matriline and patriline information for a subject/donor/sample/specimen. |

#### General Specimen Data

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`hemisphere`](#hemisphere) | exclusive_categorical | yes | hemisphere | One of two bilateral, largely symmetrical organ subdivisions within the telencephalon which contain the cerebral cortex … |
| [`left hemisphere preparation`](#left-hemisphere-preparation) | exclusive_categorical | yes | left_hemisphere_preparation | The type of preparation method used for the left hemisphere. |
| [`left hemisphere preparation specify`](#left-hemisphere-preparation-specify) | text | yes | left_hemisphere_preparation_specify | Specific details about the type of preparation method used for the left hemisphere. |
| [`left hemisphere tissue inventory`](#left-hemisphere-tissue-inventory) | — | yes | left_hemisphere_tissue_inventory | The inventory (list) of the tissue samples for a specific left hemisphere specimen. |
| [`left hemisphere tissue sampling history`](#left-hemisphere-tissue-sampling-history) | — | yes | left_hemisphere_tissue_sampling_history | The history of the tissue sampling for a specific left hemisphere specimen. |
| [`right hemisphere preparation`](#right-hemisphere-preparation) | exclusive_categorical | yes | right_hemisphere_preparation | The type of preparation method used for the right hemisphere. |
| [`right hemisphere preparation specify`](#right-hemisphere-preparation-specify) | text | yes | right_hemisphere_preparation_specify | Specific details about the type of preparation method used for the right hemisphere. |
| [`right hemisphere tissue inventory`](#right-hemisphere-tissue-inventory) | — | yes | right_hemisphere_tissue_inventory | The inventory (list) of the tissue samples for a specific right hemisphere specimen. |
| [`right hemisphere tissue sampling history`](#right-hemisphere-tissue-sampling-history) | — | yes | right_hemisphere_tissue_sampling_history | The history of the tissue sampling for a specific right hemisphere specimen. |
| [`RIN`](#rin) | numeric | yes | rin | The RNA integrity number value of a specimen. |
| [`RIN tissue source`](#rin-tissue-source) | text | yes | rin_tissue_source | The tissue sample location or identifier that is used for calculating the RNA integrity number. |
| [`RIN testing organization`](#rin-testing-organization) | text | yes | rin_testing_organization | The organization that determines the RNA integrity number of a sample/specimen. |
| [`RINe`](#rine) | numeric | yes | rine | A type of RIN (RNA integrity number) value that represents the relative ratio of the signal in the fast zone to the 18S … |
| [`RINe tissue source`](#rine-tissue-source) | text | yes | rine_tissue_source | The tissue sample location or identifier that is used for calculating the RINe number. |
| [`RINe testing organization`](#rine-testing-organization) | text | yes | rine_testing_organization | The organization that determines the RINe number. |
| [`pH`](#ph) | numeric | yes | ph | The value of a measurement of acidity or basicity of a tissue, sample, or specimen. |
| [`brain weight measurement`](#brain-weight-measurement) | numeric | yes | brain_weight | The weight of a brain specimen. |
| [`brain tissue weighed type`](#brain-tissue-weighed-type) | exclusive_categorical | yes | weighed_type | The state of a brain specimen when it is weighed (fresh, frozen, fixed). |
| [`photo 2d available`](#photo-2d-available) | exclusive_categorical | yes | photo_2d_available | The status (available, unavailable) of two-dimensional photos of a subject/donor/specimen. |

#### General Subject Fields

| Property | Type | Required | Aliases | Description |
|----------|------|----------|---------|-------------|
| [`region of interest`](#region-of-interest) | text | yes | ROI | The brain region, structure, or area from which a brain tissue source derives. |
| [`local donor ID`](#local-donor-id) | text | yes | subject_id | An identifier that uniquely denotes objects only within the scope of a specific object aggregate and that is not registe… |
| [`species`](#species) | exclusive_categorical | yes | species | The species of a subject/donor/sample/specimen. |

### Property Details

#### Family History

<div id="matriline-and-patriline" class="field-detail">
<h5><code>matriline and patriline</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>ae0447a3-0504-43a3-95d5-4248e53d3224</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> family_history</li>
</ul>
<p>The relavant matriline and patriline information for a subject/donor/sample/specimen.</p>
</div>

#### General Specimen Data

<div id="hemisphere" class="field-detail">
<h5><code>hemisphere</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>68b7a28b-d695-4ec9-800b-6a27ca206081</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> hemisphere</li>
</ul>
<p>One of two bilateral, largely symmetrical organ subdivisions within the telencephalon which contain the cerebral cortex and cerebral white matter. [UBERON]</p>
</div>

<div id="left-hemisphere-preparation" class="field-detail">
<h5><code>left hemisphere preparation</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>57d5378f-a451-4bf5-a472-cc88d0d29586</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> left_hemisphere_preparation</li>
</ul>
<p>The type of preparation method used for the left hemisphere.</p>
</div>

<div id="left-hemisphere-preparation-specify" class="field-detail">
<h5><code>left hemisphere preparation specify</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>002e915e-01c3-4570-a1f3-76680dcb2c33</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> left_hemisphere_preparation_specify</li>
</ul>
<p>Specific details about the type of preparation method used for the left hemisphere.</p>
</div>

<div id="left-hemisphere-tissue-inventory" class="field-detail">
<h5><code>left hemisphere tissue inventory</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>05e2821e-e7dc-4e33-94dc-7b55c372e5a0</code></li>
<li><strong>Aliases:</strong> left_hemisphere_tissue_inventory</li>
</ul>
<p>The inventory (list) of the tissue samples for a specific left hemisphere specimen.</p>
</div>

<div id="left-hemisphere-tissue-sampling-history" class="field-detail">
<h5><code>left hemisphere tissue sampling history</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>b02f7dd7-4535-4b41-b8df-73786b8983bc</code></li>
<li><strong>Aliases:</strong> left_hemisphere_tissue_sampling_history</li>
</ul>
<p>The history of the tissue sampling for a specific left hemisphere specimen.</p>
</div>

<div id="right-hemisphere-preparation" class="field-detail">
<h5><code>right hemisphere preparation</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>477c2600-f979-43c5-9c61-ab61fd771584</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> right_hemisphere_preparation</li>
</ul>
<p>The type of preparation method used for the right hemisphere.</p>
</div>

<div id="right-hemisphere-preparation-specify" class="field-detail">
<h5><code>right hemisphere preparation specify</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>efd50be4-f7cf-4146-a08e-28f25680728c</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> right_hemisphere_preparation_specify</li>
</ul>
<p>Specific details about the type of preparation method used for the right hemisphere.</p>
</div>

<div id="right-hemisphere-tissue-inventory" class="field-detail">
<h5><code>right hemisphere tissue inventory</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>8b6b910f-beb7-4e2b-881a-7f862ef5d588</code></li>
<li><strong>Aliases:</strong> right_hemisphere_tissue_inventory</li>
</ul>
<p>The inventory (list) of the tissue samples for a specific right hemisphere specimen.</p>
</div>

<div id="right-hemisphere-tissue-sampling-history" class="field-detail">
<h5><code>right hemisphere tissue sampling history</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>60d2efe0-bf7f-48f7-96fc-71cdf03226dd</code></li>
<li><strong>Aliases:</strong> right_hemisphere_tissue_sampling_history</li>
</ul>
<p>The history of the tissue sampling for a specific right hemisphere specimen.</p>
</div>

<div id="rin" class="field-detail">
<h5><code>RIN</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>cd472c0d-0b64-45c9-a38e-e54d15cea953</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> rin</li>
</ul>
<p>The RNA integrity number value of a specimen.</p>
</div>

<div id="rin-tissue-source" class="field-detail">
<h5><code>RIN tissue source</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>d547ee51-9ec3-489c-8e49-7d8cd94080a8</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> rin_tissue_source</li>
</ul>
<p>The tissue sample location or identifier that is used for calculating the RNA integrity number.</p>
</div>

<div id="rin-testing-organization" class="field-detail">
<h5><code>RIN testing organization</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>cfed831e-9a62-4a32-bf92-532873420eb3</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> rin_testing_organization</li>
</ul>
<p>The organization that determines the RNA integrity number of a sample/specimen.</p>
</div>

<div id="rine" class="field-detail">
<h5><code>RINe</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>1210148d-d8fb-45aa-b51a-4b19b6d09bec</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> rine</li>
</ul>
<p>A type of RIN (RNA integrity number) value that represents the relative ratio of the signal in the fast zone to the 18S peak signal fpr a specimen.</p>
</div>

<div id="rine-tissue-source" class="field-detail">
<h5><code>RINe tissue source</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>7d5fd9af-82a1-4bdb-a3c6-9225d1717c53</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> rine_tissue_source</li>
</ul>
<p>The tissue sample location or identifier that is used for calculating the RINe number.</p>
</div>

<div id="rine-testing-organization" class="field-detail">
<h5><code>RINe testing organization</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>15a6d162-a3ca-4852-b626-a911c37c04c9</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> rine_testing_organization</li>
</ul>
<p>The organization that determines the RINe number.</p>
</div>

<div id="ph" class="field-detail">
<h5><code>pH</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>9e67af02-c081-43e1-a42c-bf9603cae616</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> ph</li>
</ul>
<p>The value of a measurement of acidity or basicity of a tissue, sample, or specimen.</p>
</div>

<div id="brain-weight-measurement" class="field-detail">
<h5><code>brain weight measurement</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>546fc32d-f8a2-4c00-924a-8c4730f11f51</code></li>
<li><strong>Data Type:</strong> <code>numeric</code></li>
<li><strong>Aliases:</strong> brain_weight</li>
</ul>
<p>The weight of a brain specimen.</p>
</div>

<div id="brain-tissue-weighed-type" class="field-detail">
<h5><code>brain tissue weighed type</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>a7463e3f-0c61-4718-a7d0-60fd2116908a</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> weighed_type</li>
</ul>
<p>The state of a brain specimen when it is weighed (fresh, frozen, fixed).</p>
</div>

<div id="photo-2d-available" class="field-detail">
<h5><code>photo 2d available</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>611beda8-1ac6-4183-a284-04a30bb474f3</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> photo_2d_available</li>
</ul>
<p>The status (available, unavailable) of two-dimensional photos of a subject/donor/specimen.</p>
</div>

#### General Subject Fields

<div id="region-of-interest" class="field-detail">
<h5><code>region of interest</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>71611b58-f98e-4a69-ad88-c0029a377cbe</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> ROI</li>
</ul>
<p>The brain region, structure, or area from which a brain tissue source derives.</p>
</div>

<div id="local-donor-id" class="field-detail">
<h5><code>local donor ID</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf</code></li>
<li><strong>Data Type:</strong> <code>text</code></li>
<li><strong>Aliases:</strong> subject_id</li>
</ul>
<p>An identifier that uniquely denotes objects only within the scope of a specific object aggregate and that is not registered in an identifier registry. [Allotrope]</p>
</div>

<div id="species" class="field-detail">
<h5><code>species</code> <em>(required)</em></h5>
<ul>
<li><strong>BICAN UUID:</strong> <code>d11fb2ce-bfdb-4735-9b17-b6ba606520b1</code></li>
<li><strong>Data Type:</strong> <code>exclusive_categorical</code></li>
<li><strong>Aliases:</strong> species</li>
</ul>
<p>The species of a subject/donor/sample/specimen.</p>
</div>

<!-- schema-properties-end -->
