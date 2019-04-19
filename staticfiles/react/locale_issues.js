class Issues extends React.Component {
	constructor(props){
		super(props);

		this.state = {
			'url' : props.url,
			'loaded' : false,
			'list' : null
		}
	}

	getURL(uid){
		return '/issue/'+uid.toString()+'/';
	}

	getTimeDate(timeDate){
		return new Date(timeDate).toLocaleString();
	}

	componentDidMount(){
		fetch(this.state.url)
		.then(response => response.json())
		.then(data =>{
			console.log(data);
			const results = data.map((item) => 
				<div className="issue-card col-md-6">
				<h3 className="issue-title">{item.title}</h3>
				<small className="issue-data"><i className="fas fa-user"></i> {item.user} <i className="fas fa-calendar-alt"></i>
				{this.getTimeDate(item.time_date)}<i className="fas fa-map-marker-alt"></i>{item.address}</small>
				<p className="issue-details"></p>
				<a href={this.getURL(item.uid)} className="issue-see-more btn btn-info btn-sm">See More</a>
				<div class="row issue-interract-buttons">
					<button className="col btn btn-info"><i className="fas fa-heart"></i> Upvote (1.2M)</button>
					<button className="col btn btn-info"><i className="fas fa-comment-alt"></i> Comment (23k)</button>
				</div>
			</div>
			);

			this.setState({
				list : results,
				loaded : true
			});
		});
	}

	render(){
		if(! this.state.loaded){
			return(
				 <div>
                    <div className="spinner-grow text-muted"></div>
                    <div className="spinner-grow text-primary"></div>
                    <div className="spinner-grow text-success"></div>
                    <div className="spinner-grow text-info"></div>
                    <div className="spinner-grow text-warning"></div>
                    <div className="spinner-grow text-danger"></div>
                    <div className="spinner-grow text-secondary"></div>
                    <div className="spinner-grow text-dark"></div>
                    <div className="spinner-grow text-light"></div>
                </div>
			);
		}

		return this.state.list;
	}
}


function getURL(dom){
	return dom.getAttribute('url').toString();
}

function getRenderBlock(dom){
	return dom.getAttribute('renderID').toString();
}

const dom = document.getElementById('issue-container');
const element = (<Issues url={getURL(dom)}/>);
const block = document.getElementById(getRenderBlock(dom));

ReactDOM.render(element, block);