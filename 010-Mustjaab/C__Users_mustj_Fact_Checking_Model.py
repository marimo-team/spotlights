# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "scikit-learn==1.5.2",
#     "pandas==2.2.3",
#     "altair==5.4.1",
#     "nltk==3.9.1",
#     "marimo",
#     "plotly==5.24.1",
#     "numpy==1.26.4",
#     "gensim==4.3.3",
# ]
# ///
import marimo

__generated_with = "0.9.10"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    import numpy as np
    from gensim.models import Word2Vec
    from nltk.tokenize import word_tokenize
    import nltk
    from sklearn.model_selection import train_test_split
    from sklearn.svm import SVC
    from sklearn.metrics import accuracy_score, classification_report
    import plotly.express as px
    from sklearn.manifold import TSNE
    import altair as alt
    return (
        SVC,
        TSNE,
        Word2Vec,
        accuracy_score,
        alt,
        classification_report,
        mo,
        nltk,
        np,
        pd,
        px,
        train_test_split,
        word_tokenize,
    )


@app.cell
def __(mo):
    mo.md(
        r"""
        # Resource Fact Checking Model

        ## Table of Contents 

        - General Overview
        - Model Choice
        - Using the Model
        - Performance Analysis
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ## General Overview

        <p> The purpose of this notebook is to build a fact-checking model. We can start off simple, and add features to fortify its scalability, reliability, validity, and (relevantly) accuracy. </p>
        """
    )
    return


@app.cell
def __():
    Statement_about_Resources = [
        ("Solar energy is a renewable resource.", True),
        ("Coal is a renewable resource.", False),
        ("Wind power can be depleted.", False),
        ("Nuclear energy is considered a non-renewable resource.", True),
        ("Hydroelectric power is a form of renewable energy.", True),
        ("Natural gas is a clean, renewable resource.", False),
        ("Biomass energy comes from renewable organic materials.", True),
        ("Geothermal energy is inexhaustible.", True),
        ("Tidal energy is a type of renewable energy.", True),
        ("Fossil fuels are formed from renewable sources.", False),
        ("Wind turbines generate electricity without consuming fuel.", True),
        ("Oil reserves will replenish themselves within a human lifetime.", False),
        ("Solar panels work efficiently at night.", False),
        ("Uranium used in nuclear power plants is a renewable resource.", False),
        ("Wave energy harnesses the power of ocean surface motion.", True),
        ("Burning coal releases no greenhouse gases.", False),
        ("Hydropower relies on the water cycle, which is naturally replenished.", True),
        ("Geothermal energy taps into Earth's internal heat.", True),
        ("Wind energy production causes significant air pollution.", False),
        ("Biomass fuels are carbon-neutral.", True),
        ("Solar energy can be harnessed in cloudy weather.", True),
        ("Tidal power is predictable and consistent.", True),
        ("Nuclear fusion is currently a widely used energy source.", False),
        ("Offshore wind farms produce more energy than onshore ones.", True),
        ("Fossil fuels will never run out.", False),
        ("Photovoltaic cells convert sunlight directly into electricity.", True),
        ("Hydroelectric dams have no environmental impact.", False),
        ("Geothermal energy is only available in volcanic regions.", False),
        ("Wind turbines kill more birds than any other human activity.", False),
        ("Biomass energy always reduces greenhouse gas emissions.", False),
        ("Solar panels require more energy to produce than they generate in their lifetime.", False),
        ("Tidal barrages can affect local ecosystems.", True),
        ("Nuclear power plants produce no radioactive waste.", False),
        ("Wind energy is only viable in constantly windy areas.", False),
        ("Oil shale is a renewable energy source.", False),
        ("Concentrated solar power can store energy for nighttime use.", True),
        ("Large hydroelectric dams can cause methane emissions.", True),
        ("Geothermal power plants can trigger earthquakes.", True),
        ("Wind turbines have a lifespan of over 20 years.", True),
        ("Biomass fuels compete with food production for land use.", True),
        ("Solar energy is not viable in cold climates.", False),
        ("Tidal energy generation is widely used globally.", False),
        ("Nuclear fission produces no carbon dioxide during operation.", True),
        ("Wind energy is more expensive than fossil fuels.", False),
        ("Natural gas is the cleanest burning fossil fuel.", True),
        ("Solar farms require no water for operation.", True),
        ("Pumped-storage hydroelectricity is a form of energy storage.", True),
        ("Geothermal energy is available 24/7.", True),
        ("Wind turbines cannot operate in very high winds.", True),
        ("All biomass sources are environmentally friendly.", False),
        ("Thin-film solar cells are less efficient than traditional silicon cells.", True),
        ("Tidal energy can be harvested using underwater turbines.", True),
        ("Nuclear power plants can be powered down quickly in emergencies.", False),
        ("Vertical axis wind turbines are more efficient than horizontal axis turbines.", False),
        ("Fracking for natural gas is a completely safe process.", False),
        ("Passive solar design can reduce heating and cooling costs in buildings.", True),
        ("Run-of-river hydroelectricity always requires a large dam.", False),
        ("Enhanced geothermal systems can make geothermal energy viable in more locations.", True),
        ("Wind energy cannot be stored.", False),
        ("Algae-based biofuels are currently widely used in transportation.", False),
        ("Perovskite solar cells are a promising new technology.", True),
        ("Ocean thermal energy conversion (OTEC) works best in tropical regions.", True),
        ("Thorium reactors are widely used in nuclear power generation.", False),
        ("Airborne wind energy systems can harness high-altitude winds.", True),
        ("Shale gas is a form of renewable energy.", False),
        ("Community solar gardens allow multiple users to share solar power.", True),
        ("Micro-hydropower systems can power individual homes.", True),
        ("Geothermal heat pumps can be used for both heating and cooling.", True),
        ("Wind power cannot provide baseload power.", False),
        ("Cellulosic ethanol is made from non-food plant materials.", True),
        ("Solar thermal collectors can be used for water heating.", True),
        ("Tidal fences are less environmentally impactful than tidal barrages.", True),
        ("Breeder reactors can produce more fissile material than they consume.", True),
        ("Kite power systems are a form of wind energy.", True),
        ("Tar sands oil extraction is environmentally friendly.", False),
        ("Building-integrated photovoltaics can replace conventional building materials.", True),
        ("Small-scale hydropower always disrupts river ecosystems.", False),
        ("Hot dry rock geothermal systems require water injection.", True),
        ("Wind turbines cannot be recycled at the end of their life.", False),
        ("Biogas can be produced from animal waste.", True),
        ("Solar roads can generate electricity from streets and parking lots.", True),
        ("Wave energy converters can affect marine ecosystems.", True),
        ("Pebble bed reactors are a type of nuclear fission reactor.", True),
        ("Bladeless wind turbines produce no noise pollution.", True),
        ("Coal seam gas is a renewable resource.", False),
        ("Floatovoltaics are solar panels designed to float on water.", True),
        ("All hydroelectric power requires damming rivers.", False),
        ("Geothermal energy can be used directly for heating.", True),
        ("Wind energy production causes significant noise pollution in nearby communities.", False),
        ("Pyrolysis of biomass produces biochar, which can improve soil quality.", True),
        ("Solar updraft towers use greenhouse effect and chimney effect.", True),
        ("Tidal streams and ocean currents are the same thing.", False),
        ("Molten salt reactors are a type of nuclear fission reactor.", True),
        ("Vortex bladeless is a new type of wind energy technology.", True),
        ("Lignite is a clean-burning type of coal.", False),
        ("Agrivoltaics combines agriculture with solar energy production.", True),
        ("Pumped-storage hydroelectricity facilities can only be built in mountainous areas.", False),
        ("Ground source heat pumps can provide heating and cooling in all climates.", True),
        ("Wind turbines kill more bats than birds.", True),
        ("Biodiesel can be produced from used cooking oil.", True),
        ("Transparent solar cells can be used in windows.", True),
        ("Dynamic tidal power doesn't require a barrage or lagoon.", True),
        ("Fast breeder reactors have been widely adopted globally.", False),
        ("Airborne wind energy systems are commercially available.", False),
        ("Oil drilling in the Arctic has no environmental risks.", False),
        ("Solar thermal energy can be used for industrial processes.", True),
        ("Run-of-river hydroelectricity has less environmental impact than large dams.", True),
        ("Magma geothermal energy systems tap into underground magma chambers.", True),
        ("Offshore wind turbines are less efficient than onshore turbines.", False),
        ("Waste-to-energy plants can reduce landfill use.", True),
        ("Luminescent solar concentrators can be used in building windows.", True),
        ("Salinity gradient power harnesses energy from where rivers meet the sea.", True),
        ("Small modular reactors are currently widely used in nuclear power generation.", False),
        ("High-altitude wind power can provide more consistent energy than ground-level wind.", True),
        ("Hydraulic fracturing only uses water and sand.", False),
        ("Solar water heating systems can work in cold climates.", True),
        ("Tidal lagoons have less environmental impact than tidal barrages.", True),
        ("Deep geothermal systems can access heat at depths of several kilometers.", True),
        ("Wind turbines can increase local temperatures.", True),
        ("Biofuels always have a lower carbon footprint than fossil fuels.", False),
        ("Photovoltaic noise barriers can generate electricity along highways.", True),
        ("Marine current power is the same as tidal stream power.", False),
        ("Traveling wave reactors can use depleted uranium as fuel.", True),
        ("Kite wind generators can reach higher altitudes than traditional wind turbines.", True),
        ("Clean coal technology eliminates all pollutants from coal burning.", False),
        ("Solar canals combine water conservation with energy generation.", True),
        ("Mini-hydro systems always require construction of a dam.", False),
        ("Geothermal energy can be used for greenhouse heating in agriculture.", True),
        ("Wind turbines cannot be placed close to urban areas.", False),
        ("Torrefied biomass has properties similar to coal.", True),
        ("Solar chimneys can generate electricity in arid regions.", True),
        ("Osmotic power generates electricity from the difference in salt concentration between seawater and river water.", True),
        ("Fusion power plants are currently in commercial operation.", False),
        ("Makani power kites are a commercially successful form of wind energy.", False),
        ("Deep water oil drilling is risk-free.", False),
        ("Solar fabric can generate electricity from clothing.", True),
        ("In-stream hydro turbines always obstruct fish migration.", False),
        ("Engineered geothermal systems can make geothermal power viable in non-volcanic regions.", True),
        ("Wind turbines cannot operate in extreme cold.", False),
        ("Plasma gasification is a clean way to process municipal solid waste.", True),
        ("Photovoltaic glass can generate electricity while remaining transparent.", True),
        ("Tidal kite technology can generate power from low-velocity currents.", True),
        ("Sodium-cooled fast reactors are the most common type of nuclear reactor.", False),
        ("Crosswind kite power systems can generate more energy than traditional wind turbines.", True),
        ("Natural gas extraction never contaminates groundwater.", False),
        ("Solar balloons can generate electricity at high altitudes.", True),
        ("Micro-hydro systems are suitable for most streams and rivers.", True),
        ("Geothermal power plants always cause land subsidence.", False),
        ("Wind turbines can be harmful to human health.", False),
        ("Jatropha is a promising non-food crop for biodiesel production.", True),
        ("Solar power satellites can beam energy to Earth from space.", True),
        ("Vortex-induced vibrations can be used to generate electricity from slow water currents.", True),
        ("Liquid fluoride thorium reactors are widely used in nuclear power generation.", False),
        ("High-altitude wind kites are currently a major source of wind power.", False),
        ("Offshore oil rigs have no impact on marine ecosystems.", False),
        ("Building-integrated wind turbines can be incorporated into skyscrapers.", True),
        ("All hydroelectric dams cause significant methane emissions.", False),
        ("Shallow geothermal systems can be used for both heating and cooling buildings.", True),
        ("Wind turbines significantly reduce property values in nearby areas.", False),
        ("Microalgae can be used to produce biofuels without competing with food crops.", True),
        ("Solar roadways are currently widely implemented.", False),
        ("Underwater compressed air energy storage can be used with offshore wind farms.", True),
        ("Nuclear fusion reactors produce long-lived radioactive waste.", False),
        ("Vertical sky farms can combine wind energy with agriculture.", True),
        ("Mountaintop removal mining is an environmentally friendly way to extract coal.", False),
        ("Piezoelectric materials can generate electricity from pedestrian footsteps.", True),
        ("All small hydropower projects are environmentally benign.", False),
        ("Hot sedimentary aquifer power is a type of geothermal energy.", True),
        ("Wind turbines cause significant electromagnetic interference.", False),
        ("Biofuels derived from algae require less land than crop-based biofuels.", True),
        ("Solar greenhouses can generate electricity while growing plants.", True),
        ("Dynamic tidal power systems have been successfully implemented on a large scale.", False),
        ("Generation IV nuclear reactors are currently in wide commercial use.", False),
        ("Windbelts can generate electricity from wind without using turbines.", True),
        ("Hydraulic fracturing never causes induced seismicity.", False),
        ("Solar trees can provide both shade and electricity in urban areas.", True),
        ("Fish-friendly turbines completely eliminate fish mortality in hydroelectric systems.", False),
        ("Geothermal energy extraction always leads to the depletion of geothermal reservoirs.", False),
        ("Wind turbine syndrome is a medically recognized condition.", False),
        ("Sweet sorghum is a potential feedstock for ethanol production.", True),
        ("Space-based solar power is currently a significant source of energy on Earth.", False),
        ("Tidal fences can generate electricity without creating reservoirs.", True),
        ("Accelerator-driven subcritical reactors are commonly used for power generation.", False),
        ("Jet stream wind power is currently harnessed for electricity production.", False),
        ("Deep sea oil drilling is completely safe for marine environments.", False),
        ("Solar windows can generate electricity without significantly reducing transparency.", True),
        ("All run-of-river hydroelectric systems are free from environmental impacts.", False),
        ("Ground-source heat pumps require deep drilling in all cases.", False),
        ("Wind turbines cause significant decrease in bird populations.", False),
        ("Biofuels always produce lower greenhouse gas emissions than fossil fuels.", False),
        ("Spray-on solar cells are widely used in commercial solar panels.", False),
        ("Archimedes wave swing is a type of wave energy converter.", True),
        ("Tokamak fusion reactors are currently used for commercial power generation.", False),
        ("Kite-powered ships are widely used in commercial shipping.", False)
    ]

    Resource_Statements = [statement for statement, _ in Statement_about_Resources]
    Verification = [label for _, label in Statement_about_Resources]
    return Resource_Statements, Statement_about_Resources, Verification


@app.cell
def __(mo):
    mo.callout("Be sure to use punkt through (nltk.download('punkt')",kind='warn')
    return


@app.cell
def __(Resource_Statements, Word2Vec, word_tokenize):
    tokenized_statements = [word_tokenize(statement.lower()) for statement in Resource_Statements]

    word2vec_model = Word2Vec(sentences=tokenized_statements, vector_size=100, window=5, min_count=1, workers=4)
    return tokenized_statements, word2vec_model


@app.cell
def __(np, word2vec_model, word_tokenize):
    def document_vector(doc):
        words = word_tokenize(doc.lower())
        word_vectors = [word2vec_model.wv[word] for word in words if word in word2vec_model.wv]
        return np.mean(word_vectors, axis=0) if word_vectors else np.zeros(100)
    return (document_vector,)


@app.cell
def __(Resource_Statements, document_vector, np):
    Resource_Statements_vectors = np.array([document_vector(statement) for statement in Resource_Statements])
    return (Resource_Statements_vectors,)


@app.cell
def __(Resource_Statements_vectors, Verification, train_test_split):
    Resource_Statements_train, Resource_Statements_test, Verification_train, Verification_test = train_test_split(Resource_Statements_vectors, Verification, test_size=0.2, random_state=42)
    return (
        Resource_Statements_test,
        Resource_Statements_train,
        Verification_test,
        Verification_train,
    )


@app.cell
def __(mo):
    mo.md(
        r"""
        ## Model Choice

        <p> There's so many different classifiications model that could be used for things like fact-checking, so why a <a href = "https://scikit-learn.org/stable/modules/svm.html"> support vector machine (SVM) </a>? Well, there's a few reasons: </p>

        - SVMs are highly effective at distinguishing between different categories (in this case, verifying whether a statement is true or false) while maintaining efficiency.

        - Since we’re working with a smaller dataset, SVMs are a great choice because they perform well with limited data without sacrificing accuracy.

        - The mathematical foundation of SVMs, particularly how they create clear boundaries between categories, makes it less likely for the model to misclassify whether a statement (e.g., about natural resources) is true or false.
        """
    )
    return


@app.cell
def __(Resource_Statements_train, SVC, Verification_train):
    model = SVC(kernel='rbf', probability=True)
    model.fit(Resource_Statements_train, Verification_train)
    return (model,)


@app.cell
def __(mo):
    mo.md(r"""## Using the Model""")
    return


@app.cell
def __(mo):
    Statement = mo.ui.text(placeholder='claim', label = 'Claim about resource:').form()
    Statement
    return (Statement,)


@app.cell
def __(Statement, fact_check):
    fact_check(Statement.value)
    return


@app.cell
def __(mo):
    mo.md(r"""## Performance Analysis""")
    return


@app.cell
def __(Verification_pred, Verification_test, accuracy_score, pd):
    Accuracy_Table = pd.DataFrame({
            'Metric': ['Accuracy Score'],
            'Value':[accuracy_score(Verification_test, Verification_pred)]
    })
    Accuracy_Table
    return (Accuracy_Table,)


@app.cell
def __(
    Resource_Statements_test,
    Verification_test,
    classification_report,
    model,
):
    Verification_pred = model.predict(Resource_Statements_test)
    classification_report(Verification_test, Verification_pred)
    return (Verification_pred,)


@app.cell
def __(document_vector, model):
    def fact_check(statement):
        vectorized_statement = document_vector(statement).reshape(1, -1)
        prediction = model.predict(vectorized_statement)
        probability = model.predict_proba(vectorized_statement)[0]

        if prediction[0]:
            return f"The statement is likely true (confidence: {probability[1]:.2f})"
        else:
            return f"The statement is likely false (confidence: {probability[0]:.2f})"
    return (fact_check,)


@app.cell
def __(Resource_Statements_vectors, Verification, model, np, pd, px):
    Probabilities = model.predict_proba(Resource_Statements_vectors)

    # Create a DataFrame for plotting
    Confidence_Data = pd.DataFrame({
        'confidence': np.max(Probabilities, axis=1),
        'true_label': Verification
    })

    Model_Probability_Histogram = px.histogram(Confidence_Data,x='confidence', title = 'Histogram of Model Confidence')
    Model_Probability_Histogram
    return Confidence_Data, Model_Probability_Histogram, Probabilities


if __name__ == "__main__":
    app.run()
