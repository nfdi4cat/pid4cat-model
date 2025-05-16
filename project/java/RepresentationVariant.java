package None;

import java.util.List;
import lombok.*;



/* version: 0.3.0.post26.dev0+e73dc8d */


/**
  Data class for representations of the resource in other media types than text/html which is the default for landing_page_url.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RepresentationVariant  {

  private String variantUrl;
  private String mediaType;
  private String encodingFormat;
  private Integer size;

}
